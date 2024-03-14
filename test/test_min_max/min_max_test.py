import unittest
from src.min_max.utils import minmax

class MinMax(unittest.TestCase):
    def test_testcase1(self):
        self.assertEqual(minmax(),3)
        '''4 2
2 5
3 7
1 3
4 0
'''
    def test_testcase2(self):
        self.assertEqual(minmax(),7)
        '''2 5, 
3 7,
1 3,
4 0'''