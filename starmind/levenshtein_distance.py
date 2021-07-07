#!/usr/bin/env python3
"""Print the strings in the column of interest of a data set which are of a given distance to some given word.\n \
    ex python3 levenshtein_distance.py <file path> <column of interest> <target word> <wanted distance> or\n \
     ./levenshtein_distance.py <file path> <column of interest> <target word> <wanted distance>"""

import pandas as pd
import enchant
import re
from utils.distances import *

import argparse

parser = argparse.ArgumentParser(description="Print the strings in the column of interest of a data set which are of a given distance to some given word.\n \
    ex python3 levenshtein_distance.py <file path> <column of interest> <target word> <wanted distance> or\n \
     ./levenshtein_distance.py <file path> <column of interest> <target word> <wanted distance>")
# parser.add_argument('input', nargs='+')
parser.add_argument('string', type=str, nargs=3)
parser.add_argument('integer', type=int, nargs=1)
parser.add_argument('--debug', '-v', action='store_true')
args = parser.parse_args()
file_path = args.string[0]
col_name = args.string[1]
word = args.string[2]
wanted_distance = args.integer[0]


data = pd.read_csv(file_path)

data.dropna(subset = ['HUNDENAME'], inplace =True)
data = data[data['HUNDENAME'] != 'unbekannt']

data['cleaned_name'] = data[col_name].apply(lambda x: re.sub(r'\W+', '', x.split(' ')[0]))

data['distance'] = data['cleaned_name'].apply(lambda x: enchant.utils.levenshtein(x, word))


print(', '.join(data[data['distance'] == wanted_distance].drop_duplicates(['cleaned_name'])['cleaned_name']))

# Check my implementation
data['distance2'] = data['cleaned_name'].apply(lambda x: my_dp_levenshtein_distance(x, word))
print("My implementation gives same result: {}".format(data['distance'].equals(data['distance2'].astype('int'))))
