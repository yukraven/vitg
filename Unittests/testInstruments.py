import unittest
import Exceptions
from Instruments import getRandFromArray


class TestGetRandFromArray(unittest.TestCase):

    def testEmptyArray(self):
        with self.assertRaises(ValueError):
            getRandFromArray([])

    def testNotArray(self):
        with self.assertRaises(TypeError):
            getRandFromArray(7)

    def testValueIsNotProb(self):
        with self.assertRaises(Exceptions.ValueIsNotProbabilityError):
            getRandFromArray([50, -10, 40])

    def testIndexInArray(self):
        self.assertIn(getRandFromArray([25, 25, 25, 25]), [0, 1, 2, 3])

    def testFirstOrSecond(self):
        self.assertIn(getRandFromArray([50, 50, 0, 0]), [0, 1])

    def testSecondOrThird(self):
        self.assertIn(getRandFromArray([0, 50, 50, 0]), [1, 2])

    def testThirdOrFourth(self):
        self.assertIn(getRandFromArray([0, 0, 50, 50]), [2, 3])

    def testFirstOrFourth(self):
        self.assertIn(getRandFromArray([50, 0, 0, 50]), [0, 3])

    def testFirstGuaranteed(self):
        self.assertEqual(getRandFromArray([100, 0, 0, 0]), 0)

    def testSecondGuaranteed(self):
        self.assertEqual(getRandFromArray([0, 100, 0, 0]), 1)

    def testThirdGuaranteed(self):
        self.assertEqual(getRandFromArray([0, 0, 100, 0]), 2)

    def testFourthGuaranteed(self):
        self.assertEqual(getRandFromArray([0, 0, 0, 100]), 3)
