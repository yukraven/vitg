import unittest
from unittest import mock
import Sources.Tools.LocationLoader
import Sources.Resources.Location


class TestGetRandomLocation(unittest.TestCase):
    def setUp(self):
        self.path = "Jsons/TestLocation.json"

    def testInit(self):
        loader = Sources.Tools.LocationLoader.LocationLoader([self.path])
        assert loader.locationsNames == [["TestLocation"]]
        assert loader.unusedLocationsNames == [["TestLocation"]]

    @unittest.skip("redo")
    def testGetRandomLocation(self):
        with mock.patch.object(Sources.Resources.Location, "createLocation",
                               return_value=None) as mockMethod:
            loader = Sources.Tools.LocationLoader.LocationLoader([self.path])
            loader.getRandomLocation()

            mockMethod.assert_called_once_with("Jsons/TestLocation.json", "TestLocation")

    @unittest.skip("redo")
    def testGetNextRandomLocation(self):
        with mock.patch.object(Sources.Resources.Location, "createLocation",
                               return_value=None) as mockMethod:
            loader = Sources.Tools.LocationLoader.LocationLoader([self.path])
            loader.unusedLocationsNames[0].append("AnotherTestLocation")
            loader.unusedLocationsNames[0].pop(0)
            loader.getNextRandomLocation()

            mockMethod.assert_called_once_with(self.path, "AnotherTestLocation")


class TestCreateLocation(unittest.TestCase):
    def setUp(self):
        self.path = "Jsons/TestLocation.json"

    def testSuccess(self):
        loader = Sources.Tools.LocationLoader.LocationLoader([self.path])
        location = loader.createLocation(self.path, "TestLocation")
        dFall = 1
        wind = 2
        wet = 3
        temper = 4
        thunder = True
        ACThunder = ["Test Thunder! "]

        targetTuple = (dFall, wind, wet, temper, thunder, ACThunder)
        locationTuple = (location.dFall, location.wind, location.wet,
                         location.temper, location.thunder, location.ACthunder)

        assert targetTuple == locationTuple
