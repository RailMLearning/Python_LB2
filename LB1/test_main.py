import unittest
from main1 import sum_finder


# Тесты
class TestMath(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_finder([2,7,11,15], 9), [0,1])

    def test_2(self):
        self.assertEqual(sum_finder([3,2,4], 6), [1,2])

    def test_3(self):
        self.assertEqual(sum_finder([3,3], 6), [0,1])

    def test_4(self):
        self.assertEqual(sum_finder([2,3], 5), [0,1])

    def test_5(self):
        self.assertEqual(sum_finder([-1, -3],-4), [0,1])

    def test_6(self):
        self.assertEqual(sum_finder([1,24,7], 5), None)

    def test_7(self):
        self.assertEqual(sum_finder([1], 5), None)

    def test_8(self):
        self.assertEqual(sum_finder([1,999999999,99999999,99999999,4], 5), [0,4])

    def tefst_9(self):
        self.assertEqual(sum_finder([-234,-234,-1,-5,-5], 5), None)


if __name__ == '__main__':

    unittest.main()
