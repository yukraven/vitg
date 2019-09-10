import unittest
from unittest import mock
import Sources.Resources.Location


class TestCall(unittest.TestCase):
    def setUp(self):
        self.location = Sources.Resources.Location.Location()

        self.location.changeDFall = mock.Mock()
        self.location.changeWind = mock.Mock()
        self.location.changeWet = mock.Mock()
        self.location.changeTemper = mock.Mock()
        self.location.getThunder = mock.Mock()

    def testAllReturn(self):
        self.location.changeDFall.return_value = "1. "
        self.location.changeWind.return_value = "2. "
        self.location.changeWet.return_value = "3. "
        self.location.changeTemper.return_value = "4. "
        self.location.getThunder.return_value = "5. "

        assert self.location() == "1. 2. 3. 4. 5. "

    def testNotAllReturn(self):
        self.location.changeDFall.return_value = "1. "
        self.location.changeWind.return_value = ""
        self.location.changeWet.return_value = "3. "
        self.location.changeTemper.return_value = "4. "
        self.location.getThunder.return_value = ""

        assert self.location() == "1. 3. 4. "


class TestChangeDFall(unittest.TestCase):
    def setUp(self):
        self.location = Sources.Resources.Location.Location()
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

        Sources.Resources.Location.getRandFromArray = mock.Mock()

    def testClearToRain(self):
        Sources.Resources.Location.getRandFromArray.return_value = 1

        result = self.location.changeDFall()

        assert result == "Rain. "
        assert self.location.dFall == 1

    def testClearToClear(self):
        Sources.Resources.Location.getRandFromArray.return_value = 0

        result = self.location.changeDFall()

        assert result == ""
        assert self.location.dFall == 0

    def testRainToHail(self):
        self.location.dFall = 1
        Sources.Resources.Location.getRandFromArray.return_value = 2

        result = self.location.changeDFall()

        assert result == "Hail. "
        assert self.location.dFall == 2


class TestChangeWind(unittest.TestCase):
    def setUp(self):
        self.location = Sources.Resources.Location.Location()
        self.location.toChangeWind = {"0": []}
        self.location.ACwind = ["-30", "-20", "-10", "0", "10", "20", "30"]
        self.mods = [-30, -20, -10, 0, 10, 20, 30]

        self.location.getIndexAndMod = mock.Mock()

    def testChangeWind(self):
        for i in range(0, 6):
            with self.subTest(i=i):
                self.location.wind = 30
                self.location.getIndexAndMod.return_value = (i, self.mods[i])

                result = self.location.changeWind("random")

                assert result == self.location.ACwind[i]
                assert self.location.wind == 30 + self.mods[i]

    def testChangeWindWithMod(self):
        for i in range(0, 6):
            with self.subTest(i=i):
                self.location.wind = 30
                self.location.getIndexAndMod.return_value = (i, self.mods[i])

                result = self.location.changeWind(i)

                assert result == self.location.ACwind[i]
                assert self.location.wind == 30 + self.mods[i]

    def testChangeWindOver(self):
        for i in range(0, 2):
            with self.subTest(i=i):
                self.location.wind = 0
                self.location.getIndexAndMod.return_value = (i, self.mods[i])

                result = self.location.changeWind(i)

                assert result == self.location.ACwind[i]
                assert self.location.wind == 0
        for i in range(4, 6):
            with self.subTest(i=i):
                self.location.wind = 100
                self.location.getIndexAndMod.return_value = (i, self.mods[i])

                result = self.location.changeWind(i)

                assert result == self.location.ACwind[i]
                assert self.location.wind == 100


class TestChangeWet(unittest.TestCase):
    def setUp(self):
        self.location = Sources.Resources.Location.Location()
        self.location.toChangeWet = {"0": []}
        self.location.ACwet = ["-30", "-20", "-10", "0", "10", "20", "30"]
        self.mods = [-30, -20, -10, 0, 10, 20, 30]

        self.location.getIndexAndMod = mock.Mock()

    def testChangeWet(self):
        for i in range(0, 6):
            with self.subTest(i=i):
                self.location.wet = 30
                self.location.getIndexAndMod.return_value = (i, self.mods[i])

                result = self.location.changeWet("random")

                assert result == self.location.ACwet[i]
                assert self.location.wet == 30 + self.mods[i]

    def testChangeWetWithMod(self):
        for i in range(0, 6):
            with self.subTest(i=i):
                self.location.wet = 30
                self.location.getIndexAndMod.return_value = (i, self.mods[i])

                result = self.location.changeWet(i)

                assert result == self.location.ACwet[i]
                assert self.location.wet == 30 + self.mods[i]

    def testChangeWetOver(self):
        for i in range(0, 2):
            with self.subTest(i=i):
                self.location.wet = 0
                self.location.getIndexAndMod.return_value = (i, self.mods[i])

                result = self.location.changeWet(i)

                assert result == self.location.ACwet[i]
                assert self.location.wet == 0
        for i in range(4, 6):
            with self.subTest(i=i):
                self.location.wet = 100
                self.location.getIndexAndMod.return_value = (i, self.mods[i])

                result = self.location.changeWet(i)

                assert result == self.location.ACwet[i]
                assert self.location.wet == 100


class TestChangeTemper(unittest.TestCase):
    def setUp(self):
        self.location = Sources.Resources.Location.Location()
        self.location.toChangeTemper = {"0": []}
        self.location.ACtemper = ["-30", "-20", "-10", "0", "10", "20", "30"]
        self.mods = [-30, -20, -10, 0, 10, 20, 30]

        self.location.getIndexAndMod = mock.Mock()

    def testChangeTemper(self):
        for i in range(0, 6):
            with self.subTest(i=i):
                self.location.temper = 30
                self.location.getIndexAndMod.return_value = (i, self.mods[i])

                result = self.location.changeTemper("random")

                assert result == self.location.ACtemper[i]
                assert self.location.temper == 30 + self.mods[i]

    def testChangeTemperWithMod(self):
        for i in range(0, 6):
            with self.subTest(i=i):
                self.location.temper = 30
                self.location.getIndexAndMod.return_value = (i, self.mods[i])

                result = self.location.changeTemper(i)

                assert result == self.location.ACtemper[i]
                assert self.location.temper == 30 + self.mods[i]

    def testChangeTemperOver(self):
        for i in range(0, 2):
            with self.subTest(i=i):
                self.location.temper = 0
                self.location.getIndexAndMod.return_value = (i, self.mods[i])

                result = self.location.changeTemper(i)

                assert result == self.location.ACtemper[i]
                assert self.location.temper == 0
        for i in range(4, 6):
            with self.subTest(i=i):
                self.location.temper = 100
                self.location.getIndexAndMod.return_value = (i, self.mods[i])

                result = self.location.changeTemper(i)

                assert result == self.location.ACtemper[i]
                assert self.location.temper == 100


class TestGetIndexAndMod(unittest.TestCase):
    def setUp(self):
        self.location = Sources.Resources.Location.Location()
        self.mods = [-30, -20, -10, 0, 10, 20, 30]

        Sources.Resources.Location.getRandFromArray = mock.Mock()

    def testGetByIndex(self):
        for i in range(0, 6):
            with self.subTest(i=i):
                index, mod = self.location.getIndexAndMod([], i)

                assert index == i and mod == self.mods[i]

    def testGetByRandom(self):
        Sources.Resources.Location.getRandFromArray.return_value = 2
        index, mod = self.location.getIndexAndMod([], "random")

        assert index == 2 and mod == -10


class TestGetThunder(unittest.TestCase):
    def setUp(self):
        self.location = Sources.Resources.Location.Location()
        self.location.toThunder = [{"probability": 50, "wind": 0, "wet": 0, "temper": 0},
                                   {"probability": 50, "wind": 100, "wet": 0, "temper": 0},
                                   {"probability": 50, "wind": 0, "wet": 100, "temper": 0},
                                   {"probability": 50, "wind": 0, "wet": 0, "temper": 100}]
        self.location.ACthunder = "Thunder! "

        Sources.Resources.Location.getRandFromArray = mock.Mock()

    def testSuccess(self):
        self.location.dFall = 0
        Sources.Resources.Location.getRandFromArray.return_value = 0

        result = self.location.getThunder()

        assert result == "Thunder! "
        assert self.location.thunder

    def testFail(self):
        self.location.dFall = 0
        Sources.Resources.Location.getRandFromArray.return_value = 1

        result = self.location.getThunder()

        assert result == ""
        assert not self.location.thunder

    def testFailWind(self):
        self.location.dFall = 1
        self.location.wind = 0
        Sources.Resources.Location.getRandFromArray.return_value = 0

        result = self.location.getThunder()

        assert result == ""
        assert not self.location.thunder

    def testFailWet(self):
        self.location.dFall = 2
        self.location.wet = 0
        Sources.Resources.Location.getRandFromArray.return_value = 0

        result = self.location.getThunder()

        assert result == ""
        assert not self.location.thunder

    def testFailTemper(self):
        self.location.dFall = 3
        self.location.temper = 0
        Sources.Resources.Location.getRandFromArray.return_value = 0

        result = self.location.getThunder()

        assert result == ""
        assert not self.location.thunder


class TestTryDFall(unittest.TestCase):
    def setUp(self):
        self.location = Sources.Resources.Location.Location()
        self.location.temperFromWhich = {"rainFreezes": 20,
                                              "rainEvaporates": 80,
                                              "hailMelts": 60,
                                              "snowMelts": 60}
        self.location.wet = 0

    def testTryRainSuccess(self):
        self.location.temper = 50

        result = self.location.tryRain()

        assert result == 1
        assert self.location.wet == 30

    def testTryRainFreezes(self):
        self.location.temper = 10

        result = self.location.tryRain()

        assert result == 2
        assert self.location.wet == 0

    def testTryRainEvaporates(self):
        self.location.temper = 90

        result = self.location.tryRain()

        assert result == 0
        assert self.location.wet == 30

    def testTryHailSuccess(self):
        self.location.temper = 50

        result = self.location.tryHail()

        assert result == 2

    def testTryHailMelts(self):
        self.location.temper = 70

        result = self.location.tryHail()

        assert result == 1
        assert self.location.temper == 60

    def testTrySnowSuccess(self):
        self.location.temper = 50

        result = self.location.trySnow()

        assert result == 3

    def testTrySnowMelts(self):
        self.location.temper = 70

        result = self.location.trySnow()

        assert result == 1
        assert self.location.temper == 60
