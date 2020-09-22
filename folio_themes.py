#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Published Libraries
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
import sys

# My Library
import database

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

def folio_theme_crawler(driver, url):
  driver.get(url)
  theme_list = driver.find_element_by_id('theme-list')
  # Open all theme-list elements
  btn_themes_open = theme_list.find_element_by_id('gtm-themeboard-theme-click')
  btn_themes_open.click()
  for btn_read_more in theme_list.find_elements_by_css_selector('button.Button__sub--V901Y'):
    btn_read_more.click()
  # Read
  seq = 0
  themes = list()
  for theme in theme_list.find_elements_by_css_selector('a.gtm-theme-detail'):
    theme_id = theme.get_attribute('href').replace('https://folio-sec.com/theme/','')
    title = theme.find_element_by_css_selector('h1').text
    themes.append({'theme_id': theme_id, 'title': title, 'seq': seq})
    seq += 1
  return themes


def save(pg, themes): 
  pg.cur.execute("DELETE FROM themes")
  for theme in themes:
    pg.cur.execute("INSERT INTO themes (theme_id, title, seq ) VALUES ( %(theme_id)s, %(title)s, %(seq)s )",
     {'theme_id': theme['theme_id'], 'title': theme['title'], 'seq': theme['seq']})

if __name__ == "__main__":
  print(crawl('https://folio-sec.com/theme'))
