import unittest
from importing import sub_numbers

class TestMyModule(unittest.TestCase):

    def test_sub_numbers(self):
        result = sub_numbers(2, 3)
        self.assertEqual(result, -1)

    def test_sub_numbers_negative(self):
        result = sub_numbers(-2, 3)
        self.assertEqual(result, -5)

    def test_sub_numbers_zero(self):
        result = sub_numbers(0, 0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()