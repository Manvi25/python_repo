import unittest
from src.text_alignment.utils  import print_logo


class TextAlignment(unittest.TestCase):
    def test_testcase1(self):
        self.assertEqual(print_logo(), '''    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H     
''')

        '''5'''

    def test_testcase2(self):
        self.assertEqual(print_logo(),''' H 
HHH
 HH      HH     
 HH      HH     
 HH      HH     
 HHHHHHHHHH 
 HH      HH     
 HH      HH     
 HH      HH     
        HHH 
         H  
''')
        '''2'''

    def test_testcase3(self):
              self.assertEqual(print_logo(),'''H
H   H   
H   H   
HHHHH 
H   H   
H   H   
    H 
''')
'''1'''

if __name__ == "__main__":
    unittest.main()