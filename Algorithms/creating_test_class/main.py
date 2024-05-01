import unittest
from unit_testing import avgList


class TestAvgList(unittest.TestCase):
    def test1(self):
        list = [1, 2, 3]
        expected = 2
        self.assertEqual(avgList(list), expected, msg='avgList({})'.format(list))

    def test2(self):
        list = []
        expected = 0
        self.assertEqual(avgList(list), expected, msg='avgList({})'.format(list))


if __name__ == '__main__':
    unittest.main(verbosity=2)
