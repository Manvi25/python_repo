import unittest

from src.mean_var.utils import mean_var_std


class MyTestCase(unittest.TestCase):
    def test_testcase1(self):
        self.assertEqual(mean_var_std(), 1.11803398875)

    ''' 2 2 
            1 2
            3 4'''

    def test_testcase2(self):
        self.assertEqual(mean_var_std(), 1.224744871392)

    '''     2 4 
            7 5
            8 8'''

    def test_testcase3(self):
        self.assertEqual(mean_var_std(), 2.793842435707)

    ''' 3 6 
        8 9 
        3 4
        1 4'''


if __name__ == '__main__':
    unittest.main()