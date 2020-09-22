# webcrawler-service-job

## Overview
See [README of webcrawler-service](https://github.com/bubusuke/webcrawler-service/blob/master/README.md).

### About Folio
We are analyzing the following two types of sites.

#### 1. themes ( https://folio-sec.com/theme )
* Why: Creating theme-list.
* How: Analyzing dynamic site.
* What: Using headless Chrome and selenium. [ChromeDriver File](https://chromedriver.chromium.org/downloads) is also required.

#### 2. stocks per theme ( https://folio-sec.com/theme/${theme} )
* Why: Creating stocks-list per theme.
* How: Analyzing static site.
* What: Using beautifulsoup.

## How to build and run at local.
### 1. Preparing.
* Prepare a postgres database.
* Execute [DDL](https://github.com/bubusuke/webcrawler-service/tree/master/initdb.d). 

### 2. Exec
```sh
# Only Folio's Themes.
# In this case, database is not necessary.
# The result is desplay on STDOUT.
python3 ./folio_themes.py

# Only Folio's Theme-details.
# In this case, database is not necessary.
# The result is desplay on STDOUT.
python3 ./folio_theme_details.py

# E2E
python3 ./main.py
```
### Environments
See Job in [HERE of webcrawler-service](https://github.com/bubusuke/webcrawler-service#environments).
