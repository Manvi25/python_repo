import unittest
from src.finding_the_percentage.utils import findpercentage


class TestPercentage(unittest.TestCase):
    def test_testcase1(self):
        result = findpercentage()
        self.assertEqual(result, 56.00)
        '''
        3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
        '''
    def test_testcase2(self):
        result = findpercentage()
        self.assertEqual(result, 60.00)
        '''
        Riya 52 93 20
        Rencho 69 65 62
        Hbtg 52 60 68
        Hbtg
        '''

    def test_testcase3(self):
        result = findpercentage()
        self.assertEqual(result, 99.50)
        '''
        2
Anurag 50 60 70
Prerna 100 99.5 99
Prerna
        '''

if __name__ == "__main__":
    unittest.main()
