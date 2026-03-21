import os
import re

def check_sql_file_names(folder_path, file_name_format):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Define the regular expression pattern for the file name format
    pattern = re.compile(file_name_format)

    # Check each file name against the pattern
    for file_name in files:
        if file_name.endswith(".sql") and not pattern.match(file_name):
            print(f"File name '{file_name}' does not match the expected format.")

# Example usage
folder_path = ".."
file_name_format = r'^[a-zA-Z0-9_]+\.sql$'

check_sql_file_names(folder_path, file_name_format)
