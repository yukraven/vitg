import unittest
import Sources.Tools.Exceptions
import Sources.Tools.Instruments


class TestGetRandFromArray(unittest.TestCase):
    def testSuccess(self):
        arraysWithProbs = [[100, 0, 0, 0],
                           [0, 100, 0, 0],
                           [0, 0, 100, 0],
                           [0, 0, 0, 100]]
        arraysWithValues = [["One value. "],
                            [["One value. "]],
                            [{"One": "value"}]]
        for i in range(0, 4):
            with self.subTest(i=i):
                result = Sources.Tools.Instruments.getRandFromArray(arraysWithProbs[i], "withProbs")

                assert result == i
        for i in range(0, 3):
            with self.subTest(i=i):
                result = Sources.Tools.Instruments.getRandFromArray(arraysWithValues[i], "withValues")

                assert result == arraysWithValues[i][0]

    def testFailNotArray(self):
        array = "I'm not an array!"

        self.assertRaises(TypeError, Sources.Tools.Instruments.getRandFromArray, array, "withProbs")
        self.assertRaises(TypeError, Sources.Tools.Instruments.getRandFromArray, array, "withValues")

    def testFailEmptyArray(self):
        array = []

        self.assertRaises(ValueError, Sources.Tools.Instruments.getRandFromArray, array, "withProbs")
        self.assertRaises(ValueError, Sources.Tools.Instruments.getRandFromArray, array, "withValues")

    def testFailIsNotNumbersForWithProbs(self):
        arrays = [["", "", ""],
                  [[], [], []],
                  [{}, {}, {}]]
        for i in range(0, 3):
            with self.subTest(i=i):
                self.assertRaises(ValueError, Sources.Tools.Instruments.getRandFromArray, arrays, "withProbs")

    def testFailIsNotProbabilities(self):
        array1 = [101, 0]
        array2 = [-1, 100]

        self.assertRaises(Sources.Tools.Exceptions.ValueIsNotProbabilityError,
                          Sources.Tools.Instruments.getRandFromArray, array1, "withProbs")
        self.assertRaises(Sources.Tools.Exceptions.ValueIsNotProbabilityError,
                          Sources.Tools.Instruments.getRandFromArray, array2, "withProbs")

    def testFailSumIsNot100(self):
        array1 = [70, 40]
        array2 = [70, 20]

        self.assertRaises(Sources.Tools.Exceptions.SumOfProbabilitiesIsNot100Error,
                          Sources.Tools.Instruments.getRandFromArray, array1, "withProbs")
        self.assertRaises(Sources.Tools.Exceptions.SumOfProbabilitiesIsNot100Error,
                          Sources.Tools.Instruments.getRandFromArray, array2, "withProbs")
