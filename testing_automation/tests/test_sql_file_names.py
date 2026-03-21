import unittest
import os
import re

def is_valid_sql_file_name(file_name, pattern):
    return not file_name.endswith(".sql") or pattern.match(file_name)

class TestSQLFileNames(unittest.TestCase):

    def setUp(self):
        self.folder_path = ".."
        self.file_name_format = re.compile(r'^[a-zA-Z0-9_]+\.sql$')

    def test_sql_file_names(self):
        files = os.listdir(self.folder_path)

        for file_name in files:
            with self.subTest(file_name=file_name):
                self.assertTrue(is_valid_sql_file_name(file_name, self.file_name_format),
                                f"File name '{file_name}' does not match the expected format.")

if __name__ == '__main__':
    unittest.main()
