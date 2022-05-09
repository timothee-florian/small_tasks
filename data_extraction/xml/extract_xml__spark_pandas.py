#!/usr/bin/env python3
"""
Created on Sun May  8 20:00:18 2022

@author: Timothee-Florian
"""

from pyspark.sql import SQLContext
from pyspark.sql import SparkSession
spark  = SparkSession.builder\
                  .master("local[*]")\
                  .getOrCreate()

sc = spark.sparkContext
sqlContext = SQLContext(sc)

import pandas as pd
import xml.etree.ElementTree as ET
import argparse

def parse_xml(rdd: sc.parallelize)-> sc.parallelize:
    """Parse the xml."""
    results = []
    root = ET.fromstring(rdd[0])

    for b in root.findall('record'):
        rec = []
        rec.append(b.attrib['id'])
        for e in ['rid', 'name']:
            if b.find(e) is None:
                rec.append(None)
                continue
            value = b.find(e).text
            if e == 'price':
                value = float(value)
            rec.append(value)
        results.append(rec)
    return results


if __name__ == '__name__':
    
    parser = argparse.ArgumentParser(description='Flattening JSON')
    passparser = argparse.ArgumentParser(description='Read XML file')
    parser.add_argument('-in', '--path_xml', type = str, help = 'Path of the JSON file')
    parser.add_argument('-out', '--path_out', type = str, help = 'Path of the excel or csv file')
    
    args = parser.parse_args()
    file_rdd =sqlContext.read.text(args.path_xml, wholetext=True).rdd
    records_rdd = file_rdd.flatMap(parse_xml)
    df = records_rdd.toDF(['n', 'm', 'name']).toPandas()

    
