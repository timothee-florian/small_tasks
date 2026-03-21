#!/usr/bin/env python3

import psycopg2
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description="Read the given TABLE from the given database and write it as CSV file same name as TABLE in the current folder.\n \
    ex python3 create_csv.py <db name> <user name> <password> <TABLE name>")
parser.add_argument('input', nargs='+')
parser.add_argument('--debug', '-v', action='store_true')
args = parser.parse_args()

try:
    conn = psycopg2.connect(f"dbname='{args.input[0]}' user='{args.input[1]}' password='{args.input[2]}'")
    print("connected")
except:
    print("failed to connect")
cur = conn.cursor()

cur.execute(f'''select * from {args.input[3]};''')
apps_data = cur.fetchall()

columns = [description.name for description in cur.description]

conn.commit()
conn.close()

apps_df = pd.DataFrame.from_records(apps_data, columns = columns)

apps_df.to_csv(f'{args.input[3]}.csv.gz', index = False, compression = 'gzip')
