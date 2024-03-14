import unittest
from src.validate_email.utils import validate_mail

class MyTest(unittest.TestCase):
    def test_testcase1(self):

        self.assertEqual(validate_mail(), ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com'])
        '''
    sample input    
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
        '''

    def test_testcase2(self):

        self.assertEqual(validate_mail(), ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com'])
        '''
        sample input 
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
        '''

    def test_testcase3(self):

        self.assertEqual(validate_mail(),['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com'])
        '''
        sample input 
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
        '''

if __name__ == '__main__':
    unittest.main()