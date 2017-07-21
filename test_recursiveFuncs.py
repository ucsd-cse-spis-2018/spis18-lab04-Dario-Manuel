# test_recursiveFuncs.py

import unittest
from recursiveFuncs import recProduct 


class Test_recProduct(unittest.TestCase):
    
    def test_recProduct_1(self):
        self.assertAlmostEqual(recProduct(0,5),0)

    # Note to students: add more of these test cases
 
        
        
if __name__ == '__main__':
    unittest.main()
