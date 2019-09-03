import unittest
from unittest import mock
import Resources.Location


class TestCall(unittest.TestCase):
    def setUp(self):
        self.location = Resources.Location.Location()

        self.location.changeDFall = mock.Mock()
        self.location.changeWind = mock.Mock()
        self.location.changeWet = mock.Mock()
        self.location.changeTemperature = mock.Mock()
        self.location.getThunder = mock.Mock()

    def testAllReturn(self):
        self.location.changeDFall.return_value = "1. "
        self.location.changeWind.return_value = "2. "
        self.location.changeWet.return_value = "3. "
        self.location.changeTemperature.return_value = "4. "
        self.location.getThunder.return_value = "5. "

        assert self.location() == "1. 2. 3. 4. 5. "

    def testNotAllReturn(self):
        self.location.changeDFall.return_value = "1. "
        self.location.changeWind.return_value = ""
        self.location.changeWet.return_value = "3. "
        self.location.changeTemperature.return_value = "4. "
        self.location.getThunder.return_value = ""

        assert self.location() == "1. 3. 4. "


class TestChangeDFall(unittest.TestCase):
    def setUp(self):
        self.location = Resources.Location.Location()
        self.location.dFall = 0
        self.location.toChangeDFall = [0, 0, 0, 0]
        self.location.ACdFall = [["Clear. ", "Rain. ", "Hail. ", "Snow. "],
                                 ["Clear. ", "Rain. ", "Hail. ", "Snow. "],
                                 ["Clear. ", "Rain. ", "Hail. ", "Snow. "],
                                 ["Clear. ", "Rain. ", "Hail. ", "Snow. "]]
        self.location.tryChangeDFall = [
            lambda n: 0,
            lambda n: 1,
            lambda n: 2,
            lambda n: 3
        ]
        Resources.Location.getRandFromArray = mock.Mock()

    def testClearToRain(self):
        Resources.Location.getRandFromArray.return_value = 1

        result = self.location.changeDFall()

        assert result == "Rain. "
        assert self.location.dFall == 1

    def testClearToClear(self):
        Resources.Location.getRandFromArray.return_value = 0

        result = self.location.changeDFall()

        assert result == ""
        assert self.location.dFall == 0

    def testRainToHail(self):
        self.location.dFall = 1
        Resources.Location.getRandFromArray.return_value = 2

        result = self.location.changeDFall()

        assert result == "Hail. "
        assert self.location.dFall == 2