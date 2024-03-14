import unittest

from src.piling_up.utils import piling_up

class PilingUp(unittest.TestCase):
    def test_testcase1(self):

        self.assertEqual(piling_up(), '''Yes
No
''')
        '''
        sample input 
2
6
4 3 2 1 3 4
3
1 3 2
        '''

    def test_testcase2(self):

        self.assertEqual(piling_up(), '''Yes
No
''')
        '''
        sample input 
2
6
4 3 2 1 3 4
3
1 3 2
        '''

    def test_testcase3(self):

        self.assertEqual(piling_up(), '''No
Yes
''')
        '''
        sample input 
2
3
1 3 2
6
4 3 2 1 3 4
        '''

if __name__ == '__main__':
    unittest.main()