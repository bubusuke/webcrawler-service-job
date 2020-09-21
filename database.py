#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psycopg2

class postgres: 
    def connection(self):
        self.conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="pass", port="5432")
        self.cur = self.conn.cursor() # Use dictionary type variable
