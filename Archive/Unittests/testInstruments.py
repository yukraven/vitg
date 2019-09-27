import unittest
import Archive.Sources.Tools.Exceptions
import Archive.Sources.Tools.Instruments


class TestGetRandFromArray(unittest.TestCase):
    def testSuccess(self):
        arraysWithProbs = [[100, 0, 0, 0],
                           [0, 100, 0, 0],
                           [0, 0, 80, 0],
                           [0, 0, 0, 120]]
        arraysWithValues = [["One value. "],
                            [["One value. "]],
                            [{"One": "value"}]]
        for i in range(0, 4):
            with self.subTest(i=i):
                result = Archive.Sources.Tools.Instruments.getRandFromArray(arraysWithProbs[i], "withProbs")

                assert result == i
        for i in range(0, 3):
            with self.subTest(i=i):
                result = Archive.Sources.Tools.Instruments.getRandFromArray(arraysWithValues[i], "withValues")

                assert result == arraysWithValues[i][0]

    def testFailNotArray(self):
        array = "I'm not an array!"

        self.assertRaises(TypeError, Archive.Sources.Tools.Instruments.getRandFromArray, array, "withProbs")
        self.assertRaises(TypeError, Archive.Sources.Tools.Instruments.getRandFromArray, array, "withValues")

    def testFailEmptyArray(self):
        array = []

        self.assertRaises(ValueError, Archive.Sources.Tools.Instruments.getRandFromArray, array, "withProbs")
        self.assertRaises(ValueError, Archive.Sources.Tools.Instruments.getRandFromArray, array, "withValues")

    def testFailIsNotNumbersForWithProbs(self):
        arrays = [["", "", ""],
                  [[], [], []],
                  [{}, {}, {}]]
        for i in range(0, 3):
            with self.subTest(i=i):
                self.assertRaises(ValueError, Archive.Sources.Tools.Instruments.getRandFromArray, arrays, "withProbs")

    def testFailIsNotProbabilities(self):
        array = [-1, 100]

        self.assertRaises(Archive.Sources.Tools.Exceptions.ValueIsNotProbabilityError,
                          Archive.Sources.Tools.Instruments.getRandFromArray, array, "withProbs")
