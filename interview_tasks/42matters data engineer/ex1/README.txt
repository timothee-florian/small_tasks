Run the following scripts with their arguments:

python3 create_table_postgresql.py <db name> <user name> <password>

python3 generate_load_random_data.py <db name> <user name> <password>

python3 create_csv.py <db name> <user name> <password> <TABLE name>

python3 load_s3.py <aws_access_key_id> <aws_secret_access_key> <bucket_name> <csv_to_load> <name_csv_in_s3>

python3 load_s3_to_redshift.py <HOST redshift> <DBNAME redshift> <USER redshift> <aws password for redshift> <aws_key_id for s3> <aws_secret_access_key for s3> <csv path in s3>

Can also for all type "python script.py -h" for help

Need a local postgresql server as well as and AWS s3 and redshift 
