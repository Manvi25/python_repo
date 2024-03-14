import unittest
from src.word_order.utils import count_word_occurences

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(count_word_occurences(), "2 1 1")  # add assertion here
        '''4
                asdfg
                asdfg
                ertw
                vfsxs
                2 1 1 
                '''

    def test2(self):
        self.assertEqual(count_word_occurences(), "2 1 1")
        '''4
                asdfg
                asdfg
                ertw
                vfsxs
                2 1 1 
                '''



    def test3(self):
            self.assertEqual(count_word_occurences(), "2 1 1")

    ''' 4
            bcdef
            abcdefg
            bcde
            bcdef
            3
            2 1 1 '''




if __name__ == '__main__':
    unittest.main()