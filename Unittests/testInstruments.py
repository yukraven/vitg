import unittest
import Tools.Exceptions
import Tools.Instruments


class TestGetRandFromArray(unittest.TestCase):
    def testSuccess(self):
        arrays = [[100, 0, 0, 0],
                  [0, 100, 0, 0],
                  [0, 0, 100, 0],
                  [0, 0, 0, 100]]
        for i in range(0, 4):
            with self.subTest(i=i):
                result = Tools.Instruments.getRandFromArray(arrays[i])

                assert result == i

    def testFailNotArray(self):
        array = "I'm not array!"

        self.assertRaises(TypeError, Tools.Instruments.getRandFromArray, array)

    def testFailEmptyArray(self):
        array = []

        self.assertRaises(ValueError, Tools.Instruments.getRandFromArray, array)

    def testFailIsNotProbabilities(self):
        array1 = [101, 0]
        array2 = [-1, 100]

        self.assertRaises(Tools.Exceptions.ValueIsNotProbabilityError, Tools.Instruments.getRandFromArray, array1)
        self.assertRaises(Tools.Exceptions.ValueIsNotProbabilityError, Tools.Instruments.getRandFromArray, array2)

    def testFailSumIsNot100(self):
        array1 = [70, 40]
        array2 = [70, 20]

        self.assertRaises(Tools.Exceptions.SumOfProbabilitiesIsNot100Error, Tools.Instruments.getRandFromArray, array1)
        self.assertRaises(Tools.Exceptions.SumOfProbabilitiesIsNot100Error, Tools.Instruments.getRandFromArray, array2)
