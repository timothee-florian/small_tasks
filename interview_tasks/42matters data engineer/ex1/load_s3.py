#!/usr/bin/env python3

import boto3
import argparse

parser = argparse.ArgumentParser(description="Load random data in the TABLE 'apps' in the given database\n \
    ex python3 load_s3.py <aws_access_key_id> <aws_secret_access_key> <bucket_name> <csv_to_load> <name_csv_in_s3>")
parser.add_argument('input', nargs='+')
parser.add_argument('--debug', '-v', action='store_true')
args = parser.parse_args()


bucket_name = args.input[2]
csv_to_load = args.input[3]
name_csv_in_s3  = args.input[4]

s3 = boto3.resource(
    service_name ='s3',
    region_name = 'eu-central-1',
    aws_access_key_id = args.input[0],
    aws_secret_access_key = args.input[1]
)

s3.Bucket(bucket_name).upload_file(Filename = csv_to_load, Key = name_csv_in_s3)
