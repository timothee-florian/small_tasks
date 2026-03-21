#!/usr/bin/env python3

from datetime import datetime
import random
import string
import psycopg2
import argparse

parser = argparse.ArgumentParser(description="Load random data in the TABLE 'apps' in the given database\n \
    ex python3 generate_load_random_data.py <db name> <user name> <password>")
parser.add_argument('input', nargs='+')
parser.add_argument('--debug', '-v', action='store_true')
args = parser.parse_args()

DATETIME_FORMAT_ = "%Y-%m-%d %H:%M:%S"
N_ROWS = 5 * 10**6


def random_dates(min_date, max_date = None):
    if max_date is None:
        max_date = datetime.now()
    min_datetime = datetime.strptime(min_date, DATETIME_FORMAT_)
    min_date_seconds_1 = (min_datetime-datetime(1970, 1, 1, 1)).total_seconds()
    dif_1 = (max_date - min_datetime).total_seconds()
    delta_1 = round(dif_1 * random.random())
    date_1 = datetime.fromtimestamp( min_date_seconds_1 + delta_1 )

    date_1_seconds = (date_1- datetime(1970, 1, 1, 1)).total_seconds()
    dif_2 = (max_date - date_1).total_seconds()
    delta_2 = round(dif_2 * random.random())
    date_2 = datetime.fromtimestamp(date_1_seconds + delta_2 )
    return [date_1.strftime(DATETIME_FORMAT_), date_2.strftime(DATETIME_FORMAT_)]

def get_random_alphanumeric_string(min_length, max_length):
    length = random.randint(min_length, max_length)
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str

def create_data(n = 5 * 10**6, min_date = '2000-01-01 00:00:00'):
    while True:
        random_strings = [get_random_alphanumeric_string(40, 40) for i in range(n)] #with length of 40 the expected needed size to have a colision is arround 10^35
        if len(set(random_strings)) == n:
            break
        else:
            print('try again')
    return list(map(lambda id:  [id] +
                                [get_random_alphanumeric_string(1, 128)] + #title
                                [get_random_alphanumeric_string(1, 512)] + #description
                                random_dates(min_date, max_date = None), #puplished and last_updated
                                random_strings))

try:
    conn = psycopg2.connect(f"dbname='{args.input[0]}' user='{args.input[1]}' password='{args.input[2]}'")
    print("connected")
except:
    print("failed to connect")

cur = conn.cursor()

data = create_data(n = N_ROWS, min_date = '2000-01-01 00:00:00')


cur.executemany('''INSERT INTO apps
                                (id, title, description, published_timestamp, last_update_timestamp)
                                Values (%s, %s, %s, %s, %s)''', data)

conn.commit()
conn.close()
