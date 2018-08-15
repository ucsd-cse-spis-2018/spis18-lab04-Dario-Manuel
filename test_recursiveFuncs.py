# test_recursiveFuncs.py

import unittest
from recursiveFuncs import recProduct


class Test_recProduct(unittest.TestCase):

    def test_recProduct_1(self):
        self.assertAlmostEqual(recProduct(0,5),0)
    def test_recProduct_2(self):
        self.assertAlmostEqual(recProduct(-1,5),-5)
    def test_recProduct_3(self):
        self.assertAlmostEqual(recProduct(100,6),600)
    def test_recProduct_4(self):
        self.assertAlmostEqual(recProduct(3,9),27)

    # Note to students: add more of these test cases



if __name__ == '__main__':
    unittest.main()
