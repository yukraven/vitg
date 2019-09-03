import unittest
from unittest import mock
from Resources.Location import Location


class TestCall(unittest.TestCase):
    @mock.patch('''''''''''''''''''''''''''''''''''')
    def testConduct(self, mockLocation):
        mockLocation.changeDFall.return_value = "1. "
        mockLocation.changeWind.return_value = "2. "
        mockLocation.changeWet.return_value = "3. "
        mockLocation.changeTemperature.return_value = "4. "
        mockLocation.getThunder.return_value = "5. "
        mockLocation.__call__ = Location.__call__
        assert mockLocation() == "1. 2. 3. 4. 5."
