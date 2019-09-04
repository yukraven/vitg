import unittest
from unittest import mock
import Tools.LocationLoader
import Resources.Location


class TestGetRandomLocation(unittest.TestCase):
    def setUp(self):
        self.path = "Jsons/TestLocation.json"

    def testInit(self):
        loader = Tools.LocationLoader.LocationLoader([self.path])
        assert loader.locationsNames == [["TestLocation"]]
        assert loader.unusedLocationsNames == [["TestLocation"]]

    def testGetRandomLocation(self):
        with mock.patch.object(Tools.LocationLoader.LocationLoader, "createLocationByName",
                               return_value=None) as mockMethod:
            loader = Tools.LocationLoader.LocationLoader([self.path])
            loader.getRandomLocation()

            mockMethod.assert_called_once_with("Jsons/TestLocation.json", "TestLocation")

    def testGetNextRandomLocation(self):
        with mock.patch.object(Tools.LocationLoader.LocationLoader, "createLocationByName",
                               return_value=None) as mockMethod:
            loader = Tools.LocationLoader.LocationLoader([self.path])
            loader.unusedLocationsNames[0].append("AnotherTestLocation")
            loader.unusedLocationsNames[0].pop(0)
            loader.getNextRandomLocation()

            mockMethod.assert_called_once_with(self.path, "AnotherTestLocation")

    def testCreateLocationByName(self):
        loader = Tools.LocationLoader.LocationLoader([self.path])
        location = loader.createLocationByName(self.path, "TestLocation")
        dFall = 1
        wind = 2
        wet = 3
        temperature = 4
        thunder = True
        ACThunder = "Test Thunder! "

        targetTuple = (dFall, wind, wet, temperature, thunder, ACThunder)
        locationTuple = (location.dFall, location.wind, location.wet,
                         location.temperature, location.thunder, location.ACthunder)

        assert targetTuple == locationTuple
