#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psycopg2
import os
class postgres: 
    def connection(self):
        host = os.environ.get('DB_HOST','localhost')
        port = os.environ.get('DB_PORT','5432')
        dbname = os.environ.get('DB_DATABASE_NAME','postgres')
        user = os.environ.get('DB_USER','postgres')
        password = os.environ.get('DB_PASSWORD','pass')

        print(f'host={host}, dbname={dbname}, user={user}, password={password}, port={port}')
        self.conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port  )
        self.cur = self.conn.cursor() # Use dictionary type variable
