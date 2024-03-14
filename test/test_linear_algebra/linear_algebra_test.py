import unittest
from src.linear_algebra.utils import determinant
class Determinant(unittest.TestCase):
    def test_testcase1(self):
        self.assertEqual(determinant(),0.0)
        '''2
1.1 1.1
1.1 1.1'''

    def test_testcase2(self):
        self.assertEqual(determinant(),0.11)
        '''2
1.1 1.1
1.1 1.2'''

    def test_testcase3(self):
        self.assertEqual(determinant(),6.0)
        '''3
1 2 3
4 5 6
1 2 1'''