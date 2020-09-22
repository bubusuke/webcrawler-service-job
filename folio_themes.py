#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Published Libraries
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
import sys

# My Library
import database

# "crawl" is analyzed using headless Chrome and selenium because the target site needed to be analyzed as a dynamic site, 
# It requires ChromeDriver File.
# Please install the ChromeDriver according to each development environment.
# See https://chromedriver.chromium.org/downloads.
def crawl(url):
  options = ChromeOptions()
  options.add_argument('--headless')
  options.add_argument('--no-sandbox')
  options.add_argument('--disable-dev-shm-usage')
  driver = Chrome(options=options)

  print('Start to crawl. url:' + url)
  themes = folio_theme_crawler(driver, url)
  driver.quit()

  if len(themes) == 0:
    print ('Failed to crawl the theme page. Check the structure on the following page.')
    print (url)
    sys.exit(1)

  print('Success to crawl the theme page.')
  print('The Number of themes is '+ str(len(themes)))

  return themes

# "folio_theme_crawler" represents site operation and analysis.
def folio_theme_crawler(driver, url):
  driver.get(url)
  theme_list = driver.find_element_by_id('theme-list')

  # Open all theme-list elements (Dynamic-site).
  btn_themes_open = theme_list.find_element_by_id('gtm-themeboard-theme-click')
  btn_themes_open.click()
  for btn_read_more in theme_list.find_elements_by_css_selector('button.Button__sub--V901Y'):
    btn_read_more.click()

  # Read and parse.
  seq = 0
  themes = list()
  for theme in theme_list.find_elements_by_css_selector('a.gtm-theme-detail'):
    theme_id = theme.get_attribute('href').replace(url+'/','')
    title = theme.find_element_by_css_selector('h1').text
    themes.append({'theme_id': theme_id, 'title': title, 'seq': seq})
    seq += 1
  return themes


# "save" stores themes.
# Old data is not needed, so DELETE-INSERT the data.
def save(pg, themes): 
  pg.cur.execute("DELETE FROM themes")
  for theme in themes:
    pg.cur.execute("INSERT INTO themes (theme_id, title, seq ) VALUES ( %(theme_id)s, %(title)s, %(seq)s )",
     {'theme_id': theme['theme_id'], 'title': theme['title'], 'seq': theme['seq']})

# For test.
if __name__ == "__main__":
  print(crawl(os.environ.get('URL_FOLIO','https://folio-sec.com/theme')))
