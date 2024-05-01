from contrived_func import contrived_func
import unittest


class ContrivedFuncCoverageTests(unittest.TestCase):

    # Tests True for (100, 150)
    def test1(self):
        val = 125
        self.assertTrue(contrived_func(val))

    # Tests True for val == 6
    def test2(self):
        val = 6
        self.assertFalse(contrived_func(val))

    # Tests False for val == 6
    def test3(self):
        val = 5
        self.assertTrue(contrived_func(val))

    # Tests True for first inequality and False for the second
    def test4(self):
        val = 59
        self.assertFalse(contrived_func(val))

    # Tests False for the modulus
    def test5(self):
        val = 99
        self.assertFalse(contrived_func(val))

    # Tests True for the modulus
    def test6(self):
        val = 250
        self.assertTrue(contrived_func(val))

    # Tests False for the first 'or' inequality
    def test7(self):
        val = 75
        self.assertTrue(contrived_func(val))


if __name__ == '__main__':
    unittest.main()
