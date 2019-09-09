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

    def testGetRandomLocation(self):
        with mock.patch.object(Sources.Resources.Location, "createLocation",
                               return_value=None) as mockMethod:
            loader = Sources.Tools.LocationLoader.LocationLoader([self.path])
            loader.getRandomLocation()

            mockMethod.assert_called_once_with("Jsons/TestLocation.json", "TestLocation")

    def testGetNextRandomLocation(self):
        with mock.patch.object(Sources.Resources.Location, "createLocation",
                               return_value=None) as mockMethod:
            loader = Sources.Tools.LocationLoader.LocationLoader([self.path])
            loader.unusedLocationsNames[0].append("AnotherTestLocation")
            loader.unusedLocationsNames[0].pop(0)
            loader.getNextRandomLocation()

            mockMethod.assert_called_once_with(self.path, "AnotherTestLocation")
