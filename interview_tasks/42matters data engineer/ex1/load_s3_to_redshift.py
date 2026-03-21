#!/usr/bin/env python3

import psycopg2
import argparse

PORT = '5439'
REGION = 'eu-central-1'


parser = argparse.ArgumentParser(description="Load s3 csv to redshift TABLE 'apps'\n \
    ex python3 load_s3_to_redshift.py <host for redshift> <DBNAME redshift> <USER redshift> <aws password for redshift>\
    <aws_key_id for s3> <aws_secret_access_key for s3> <csv path in s3>")
parser.add_argument('input', nargs='+')
parser.add_argument('--debug', '-v', action='store_true')
args = parser.parse_args()


conn=psycopg2.connect(dbname = args.input[1], host = args.input[0],
                     port = PORT, user = args.input[2], password = args.input[3])

cur = conn.cursor()


cur.execute(f"""CREATE TABLE IF NOT EXISTS apps (
  pk              INT PRIMARY KEY,
  id              VARCHAR(256) NOT NULL,
  title           VARCHAR(256),
  description     VARCHAR(2000),
  published_timestamp TIMESTAMP,
  last_update_timestamp TIMESTAMP);""")

conn.commit()


load_table = f"""copy apps from 's3://{args.input[6]}'
            credentials 'aws_access_key_id={args.input[4]};aws_secret_access_key={args.input[5]}'
            csv gzip ignoreheader 1"""


cur.execute(load_table)
conn.commit()
conn.close()
