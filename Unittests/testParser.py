import unittest
from unittest import mock
import Sources.Parser


class TestGetActions(unittest.TestCase):
    def setUp(self):
        self.actions = ["test1", "test1", "test1"]
        self.message = "test1 test2 test3"
        self.calls = [mock.call("test1"), mock.call("test2"), mock.call("test3")]
        self.parser = Sources.Parser.Parser()

    def testSuccess(self):
        actions = self.parser.getActions(self.message)
        assert self.actions == actions

        self.parser.getCommand = mock.Mock()
        self.parser.getCommand.assert_called()

        temp = mock.Mock(return_value="test1")
        temp.assert_called()