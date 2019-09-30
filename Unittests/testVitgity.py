import unittest
from unittest import mock
import Sources.Vitgity


class TestInit(unittest.TestCase):
    def testSuccess(self):
        dictionary = {"name": "1", "startDescription": "2", "description": "3", "speed": 4, "actions": ["wait"]}

        vitgity = Sources.Vitgity.Vitgity(dictionary)
        assert vitgity.name == "1"
        assert vitgity.startDescription == "2"
        assert vitgity.description == "3"
        assert vitgity.speed == 4
        assert vitgity.actions["wait"] == vitgity.wait

    def testSuccessButNoMethodForAction(self):
        dictionary = {"name": "1", "startDescription": "2", "description": "3", "speed": 4,
                      "actions": ["Not a correct action"]}

        vitgity = Sources.Vitgity.Vitgity(dictionary)
        assert vitgity.name

    def testNotDictionary(self):
        dictionaries = [[1, 2, 3],
                        1,
                        "1"]
        for i in range(len(dictionaries)):
            with self.subTest(i=i):
                vitgity = Sources.Vitgity.Vitgity(dictionaries[i])
                assert vitgity.name == "ErrorLoad"
                assert vitgity.description == "Bad argument"

    def testWrongData(self):
        dictionaries = [{"name": 1, "startDescription": "2", "description": "3", "speed": 4, "actions": ["wait"]},
                        {"name": "1", "startDescription": 2, "description": "3", "speed": 4, "actions": ["wait"]},
                        {"name": "1", "startDescription": "2", "description": 3, "speed": 4, "actions": ["wait"]},
                        {"name": "1", "startDescription": "2", "description": "3", "speed": "4", "actions": ["wait"]},
                        {"name": "1", "startDescription": "2", "description": "3", "speed": 4, "actions": 5},
                        {"name": "1", "startDescription": "2", "description": "3", "speed": 4, "actions": [5]},

                        {"startDescription": "2", "description": "3", "speed": 4, "actions": ["wait"]},
                        {"name": "1", "description": "3", "speed": 4, "actions": ["wait"]},
                        {"name": "1", "startDescription": "2", "speed": 4, "actions": ["wait"]},
                        {"name": "1", "startDescription": "2", "description": "3", "actions": ["wait"]},
                        {"name": "1", "startDescription": "2", "description": "3", "speed": 4}]
        errors = ["name", "startDescription", "description", "speed", "actions", "actions"
                  "name", "startDescription", "description", "speed", "actions"]

        dictionaryForManyErrors = {"name": "1", "description": "3", "speed": "4"}
        errorArray = ["startDescription", "speed", "actions"]

        for i in range(len(dictionaries)):
            with self.subTest(i=i):
                vitgity = Sources.Vitgity.Vitgity(dictionaries[i])
                assert vitgity.name == "ErrorLoad"
                assert vitgity.description[0] == errors[i]

        vitgity = Sources.Vitgity.Vitgity(dictionaryForManyErrors)
        assert vitgity.name == "ErrorLoad"
        assert vitgity.description == errorArray
