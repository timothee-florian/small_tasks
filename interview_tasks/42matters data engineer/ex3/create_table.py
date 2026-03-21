#!/usr/bin/env python3
import psycopg2
import argparse

parser = argparse.ArgumentParser(description="Create the requested TABLE 'apps' in the given database add index for future query\n \
    ex python3 create_table.py <db name> <user name> <password>")
parser.add_argument('input', nargs='+')
parser.add_argument('--debug', '-v', action='store_true')
args = parser.parse_args()

try:
    conn = psycopg2.connect(f"dbname='{args.input[0]}' user='{args.input[1]}' password='{args.input[2]}'")
    print("connected")
except:
    print("failed to connect")
cur = conn.cursor()

create_table = '''CREATE TABLE apps (
  pk                    SERIAL PRIMARY KEY,
  id                    VARCHAR(256) NOT NULL,
  title                 VARCHAR(256),
  rating                NUMERIC(2,1),
  last_update_date TIMESTAMP);'''

inserts = ["""INSERT INTO apps(id, title, rating, last_update_date)
VALUES ('com.facebook.katana', 'Facebook', 4.0, '2016-09-12');""",
"""INSERT INTO apps(id, title, rating, last_update_date)
VALUES ('com.whatsapp', 'WhatsApp', 4.5, '2016-09-11');""",

"""INSERT INTO apps(id, title, rating, last_update_date)
VALUES ('com.whatsapp', 'WhatsApp', 4.4, '2016-09-12');""",
"""INSERT INTO apps(id, title, rating, last_update_date)
VALUES ('com.nianticlabs.pokemongo', 'Pokémon GO', 4.6, '2016-09-05');""",

"""INSERT INTO apps(id, title, rating, last_update_date)
VALUES ('com.nianticlabs.pokemongo', 'Pokémon GO', 4.3, '2016-09-06');""",
"""INSERT INTO apps(id, title, rating, last_update_date)
VALUES ('com.nianticlabs.pokemongo', 'Pokémon GO', 4.1, '2016-09-07');"""]


add_index = """CREATE INDEX test2_mm_idx ON apps (id, last_update_date);"""



cur.execute(create_table)
conn.commit()

for insert in inserts:
    cur.execute(insert)
    conn.commit()

cur.execute(add_index)
conn.commit()
conn.close()
print('done')
