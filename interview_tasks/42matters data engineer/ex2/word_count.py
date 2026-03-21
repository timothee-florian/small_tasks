#!/usr/bin/env python3
"""Word count using pyspark of a file given as argument.
ex python3 word_count.py <file path> or ./word_count.py <file path>"""

from pyspark.sql import SparkSession
from pyspark import SparkContext
from nltk.tokenize import WhitespaceTokenizer
import pandas as pd

import argparse

parser = argparse.ArgumentParser(description="Counts words using Spark of a file given as argument.\n \
    ex python3 word_count.py <file path> or ./word_count.py <file path>")
parser.add_argument('input', nargs='+')
parser.add_argument('--debug', '-v', action='store_true')
args = parser.parse_args()

spark = SparkSession.builder.\
    master("local[*]").\
    appName("word_count").getOrCreate()

sc = spark.sparkContext

text = sc.textFile(args.input[0]) #read file whose name is given as argument

tk = WhitespaceTokenizer()
lines = text.filter(lambda line: line.startswith('BG:'))
words = lines.flatMap(lambda line: tk.tokenize(line)) #keep 'BG:' as a word

words_count = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

# save word count to a csv
df = pd.DataFrame(words_count.collect(), columns =['Word', 'Count'])
df.to_csv('word_count.csv', index = False)

sc.stop()
