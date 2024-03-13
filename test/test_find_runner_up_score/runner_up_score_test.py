import unittest
from src.find_runner_up_score.utils import runner_up
class RunnerUp(unittest.TestCase):
    def test_testcase1(self):
        second_max= runner_up()
        self.assertEqual(second_max, 5)
        '''5
2 3 6 6 5'''
    def test_testcase2(self):
        second_max= runner_up()
        self.assertEqual(second_max,-57)
        '''4
57 57 -57 57'''
    def test_testcase3(self):
        second_max = runner_up()
        self.assertEqual(second_max, 5)
        '''10
6 6 6 6 6 6 6 6 6 5'''

if __name__ == "__main__":
    unittest.main()



