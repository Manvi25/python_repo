import unittest
from src.string_merge.utils import merge_the_tools

class MergeTools(unittest.TestCase):
    def test_testcase1(self):
        self.assertEqual(merge_the_tools(),'''AB
CA
AD
''')

    def test_testcase2(self):
        self.assertEqual(merge_the_tools(), '''XYZ
    WXY
    Z
    ''')

    def test_testcase3(self):
        self.assertEqual(merge_the_tools(), '''DES
        WED
        W
       ''')