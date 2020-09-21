#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import folio_themes
import folio_theme_details
import database

def main():
  theme_url = 'https://folio-sec.com/theme'

  #crawler
  print('Start to crawle.')
  themes = folio_themes.crawl(theme_url)
  theme_details = list()
  for theme in themes:
    theme_details.extend(folio_theme_details.crawl(theme_url, theme))

  #save
  print('saving..')
  pg = database.postgres()
  pg.connection()
  folio_themes.save(pg, themes)
  folio_theme_details.save(pg, theme_details)
  pg.conn.commit()
  pg.conn.close()
  print('Success to save..')

if __name__ == "__main__":
  main()
