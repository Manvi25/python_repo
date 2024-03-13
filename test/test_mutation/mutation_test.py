import unittest
from src.string_mutation.utils import string_mutation

class StringMutation(unittest.TestCase):
    def test_testcase1(self):
        self.assertEqual(string_mutation(),'abrackdabra' )
        '''abracadabra
5 k'''

    def test_testcase2(self):
            self.assertEqual(string_mutation(), 'maavikhandelwal')
            '''manvikhandelwal
    2 a'''

    def test_testcase3(self):
        self.assertEqual(string_mutation(), 'testcase')
        '''testcase
1 s'''