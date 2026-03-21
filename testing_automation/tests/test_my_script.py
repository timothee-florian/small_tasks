# tests/test_my_script.py
import unittest

class TestMyScript(unittest.TestCase):

    def test_script_runs_without_errors(self):
        try:
            import importing
        except Exception as e:
            self.fail(f"Failed to import my_script: {e}")

if __name__ == '__main__':
    unittest.main()
