import unittest
from unittest import mock
import Sources.Parser


class TestGetListOfWords(unittest.TestCase):
    def setUp(self):
        self.usualMessage = "one ONE"
        self.withMarks = ["one%s %sone" % (i, i) for i in [".", ",", "!", "?"]]
        self.result = ["one", "one"]
        self.numbers = "1 2 3 4"
        self.resultNumbers = ["1", "2", "3", "4"]
        self.severalMarks = "one.two,three!"
        self.resultSeveralMarks = ["one", "two", "three"]
        self.parser = Sources.Parser.Parser()

    def testUsualMessage(self):
        listOfWords = self.parser.getListOfWords(self.usualMessage)
        difference = list(set(self.result) ^ set(listOfWords))
        assert not difference

    def testNumbers(self):
        listOfWords = self.parser.getListOfWords(self.numbers)
        difference = list(set(self.resultNumbers) ^ set(listOfWords))
        assert not difference

    def testSeveralMarks(self):
        self.parser.splitByMarks = mock.Mock(return_value=["one", "two", "three"])
        listOfWords = self.parser.getListOfWords(self.severalMarks)
        difference = list(set(self.resultSeveralMarks) ^ set(listOfWords))
        assert not difference

    def testWithMarks(self):
        self.parser.splitByMarks = mock.Mock(return_value=["one"])
        for i in range(4):
            with self.subTest(i=i):
                listOfWords = self.parser.getListOfWords(self.withMarks[i])
                difference = list(set(self.result) ^ set(listOfWords))
                assert not difference


class TestGetActions(unittest.TestCase):
    def setUp(self):
        self.actions = ["test", "test", "test"]
        self.message = "test1 test2 test3"
        self.parser = Sources.Parser.Parser()
        self.parser.encode = mock.Mock(return_value="test")
        self.parser.getListOfWords = mock.Mock(return_value=["test1", "test1", "test1"])

    def testSuccess(self):
        actions = self.parser.getActions(self.message)
        difference = list(set(self.actions) ^ set(actions))
        assert not difference


class TestSplitByMarks(unittest.TestCase):
    def setUp(self):
        self.word = "one.two,three!four?five"
        self.result = ["one", "two", "three", "four", "five"]
        self.parser = Sources.Parser.Parser()
