# webcrawler-service-job

## Overview
See [README of webcrawler-service](https://github.com/bubusuke/webcrawler-service/blob/master/README.md).

## How to build and run at local.
### 1. Preparing.
* Prepare a postgres database.
* Execute [DDL](https://github.com/bubusuke/webcrawler-service/tree/master/initdb.d). 

### 2. Exec
```
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
