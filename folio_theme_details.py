#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def crawl(url, target_theme):

  theme_id = target_theme['theme_id']
  target_url = url+'/'+theme_id
  print('Start to crawl. url:' + target_url)

  bs = BeautifulSoup(requests.get(target_url).content, 'html.parser')
  theme_details = list()
  id = 0
  for tb in bs.find_all('table'):
    for el in tb.find_all('button', class_='gtm-stock-detail'):
      theme_details.append({'theme_id': theme_id, 'detail_id': id, 'title':el.text})
      id += 1

  print('Success to crawl. details:' + str(len(theme_details)))

  return theme_details

def save(pg, theme_details): 
  pg.cur.execute("DELETE FROM theme_details")
  for theme_detail in theme_details:
    pg.cur.execute("INSERT INTO theme_details (theme_id, detail_id, title) VALUES ( %(theme_id)s, %(detail_id)s, %(title)s )",
     {'theme_id': theme_detail['theme_id'], 'detail_id': theme_detail['detail_id'], 'title': theme_detail['title']})


if __name__ == "__main__":
  print(crawl('https://folio-sec.com/theme', 'pay'))
