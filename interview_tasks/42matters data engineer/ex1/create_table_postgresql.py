#!/usr/bin/env python3

import psycopg2
import argparse

parser = argparse.ArgumentParser(description="Create the requested TABLE 'apps' in the given database\n \
    ex python3 create_table_postgresql.py <db name> <user name> <password>")
parser.add_argument('input', nargs='+')
parser.add_argument('--debug', '-v', action='store_true')
args = parser.parse_args()

try:
    conn = psycopg2.connect(f"dbname='{args.input[0]}' user='{args.input[1]}' password='{args.input[2]}'")
    print("connected")
except:
    print("failed to connect")

cur = conn.cursor()

cur.execute('''CREATE TABLE apps (
  pk                    SERIAL PRIMARY KEY,
  id                    VARCHAR(256) NOT NULL UNIQUE,
  title                 VARCHAR(256),
  description           VARCHAR(2000),
  published_timestamp   TIMESTAMP,
  last_update_timestamp TIMESTAMP);''')


conn.commit()
conn.close()
