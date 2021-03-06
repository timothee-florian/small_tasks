#!/usr/bin/env python3
"""
Created on Fri May  28 23:58:57 2022

@author: Timothee-Florian

Functions to retrieve the name of the schemas, tables, and columns in a SQL query
"""

import re
import argparse
parser = argparse.ArgumentParser(description='read a SQL script and retrieve the name of the schemas, tables and columns')
parser.add_argument('-sql', '--sql', type = str, help = 'Path of the SQL script')
parser.add_argument('-t', '--target', type = str, help = 'waht are researched Schema (s), Tables (t) or columns (c) not necessary unique eg. ct will retrieve both columns and tables name')
parser.add_argument('-s', '--separator', type = str, help = 'separation between the outputs default return line', default= '\n')
parser.add_argument('-out', '--path_out', type = str, help = 'Path of the text file containing the researched data')
args = parser.parse_args()

with open(args.sql, 'r') as f:
    text = f.read()

text =  text.replace('''"''', '')

parent_child = re.findall('''\w{1}[\w0-9]*\.\w{1}[a-zA-Z_0-9]*''', text)

parents = set(map(lambda x: x.split('.')[0], parent_child))
childs = set(map(lambda x: x.split('.')[1], parent_child))

schemas = parents - childs
columns = childs -  parents 
tables = parents.intersection(childs)


if set(args.target) == set('tcs'):
    out = list(schemas.union(tables.union(columns)))
elif 's' in args.target and 't' in args.target and 'c' not in args.target:
    out = list(filter(lambda x: x.split('.')[0] in schemas, parent_child))

elif 'c' in args.target and 't' in args.target and 's' not in args.target:
    out = list(filter(lambda x: x.split('.')[1] in columns, parent_child))

elif 's' in args.target:
    out = list(schemas)
elif 'c' in args.target:
    out = list(columns)
elif 't' in args.target:
    out = list(tables)

with open(args.path_out, 'w') as f:
    f.write(args.separator.join(out))