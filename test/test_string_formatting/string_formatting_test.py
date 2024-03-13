import unittest
from src.string_formatting.utils import print_formatted

class StringFormatting(unittest.TestCase):
     def test_testcase1(self):
         self.assertEqual(print_formatted(), '''\n1 1 1 1\n''')

if __name__ == "__main__":
    unittest.main()