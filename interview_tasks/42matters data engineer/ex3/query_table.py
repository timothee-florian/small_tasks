#!/usr/bin/env python3
import psycopg2
import argparse
import pandas as pd

parser = argparse.ArgumentParser(description="Query the requested TABLE 'apps' in the given database to get the latest update of each app. Save in csv\n \
    ex python3 query_table.py <db name> <user name> <password> <csv name>")
parser.add_argument('input', nargs='+')
parser.add_argument('--debug', '-v', action='store_true')
args = parser.parse_args()

try:
    conn = psycopg2.connect(f"dbname='{args.input[0]}' user='{args.input[1]}' password='{args.input[2]}'")
    print("connected")
except:
    print("failed to connect")
cur = conn.cursor()


query = """SELECT pk, gapps.id, title, rating, last_update_date
        FROM apps
          INNER JOIN
          (
            SELECT id, MAX(last_update_date) last_date
            FROM apps
            GROUP BY id
          ) gapps
          ON apps.id = gapps.id
        WHERE apps.last_update_date = gapps.last_date;
        """

cur.execute(query)
apps_data = cur.fetchall()

columns = [description.name for description in cur.description]

conn.commit()
conn.close()

apps_df = pd.DataFrame.from_records(apps_data, columns = columns)

apps_df.to_csv(f'{args.input[3]}.csv', index = False)
print('done')
