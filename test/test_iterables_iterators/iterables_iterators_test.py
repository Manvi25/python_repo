import unittest
from src.iterables_iterators.utils import iterables_iterators

class IterablesIterators(unittest.TestCase):
    def test_testcase1(self):
        self.assertEqual(iterables_iterators(),0.833333)
        '''4
 a a c d
 2'''
    def test_testcase2(self):
         self.assertEqual(iterables_iterators(), 0.722222)
         '''9
 a b c a d b z e o
 4'''





