import unittest
import Sources.Vitgities.Vitgity


class TestInit(unittest.TestCase):
    def testSuccess(self):
        dictionary = {"name": "1", "startDescription": "2", "description": "3", "speed": 4, "actions": ["wait"]}

        vitgity = Sources.Vitgities.Vitgity.Vitgity(dictionary)
        assert vitgity.name == "1"
        assert vitgity.startDescription == "2"
        assert vitgity.description == "3"
        assert vitgity.speed == 4
        assert vitgity.actions == ["wait"]

    def testBadData(self):
        dictionaries = [["name", "startDescription", "description", "speed", "actions"],

                        {"name": 1, "startDescription": "2", "description": "3", "speed": 4, "actions": ["wait"]},
                        {"name": "1", "startDescription": 2, "description": "3", "speed": 4, "actions": ["wait"]},
                        {"name": "1", "startDescription": "2", "description": 3, "speed": 4, "actions": ["wait"]},
                        {"name": "1", "startDescription": "2", "description": "3", "speed": "str", "actions": ["wait"]},

                        {"name": "1", "startDescription": "2", "description": "3", "speed": 4, "actions": 5},
                        {"name": "1", "startDescription": "2", "description": "3", "speed": 4, "actions": [5]},

                        {"startDescription": "2", "description": "3", "speed": 4, "actions": ["wait"]},
                        {"name": "1", "description": "3", "speed": 4, "actions": ["wait"]},
                        {"name": "1", "startDescription": "2", "speed": 4, "actions": ["wait"]},
                        {"name": "1", "startDescription": "2", "description": "3", "actions": ["wait"]},
                        {"name": "1", "startDescription": "2", "description": "3", "speed": 4},

                        {"name": "1", "description": "3", "speed": "4"}]

        for i in range(len(dictionaries)):
            with self.subTest(i=i):
                vitgity = Sources.Vitgities.Vitgity.Vitgity(dictionaries[i])
                assert vitgity.name == "ErrorLoad"


class TestGetUp(unittest.TestCase):
    def testSuccess(self):
        result = "Some information"
        dictionary = {"name": "1", "startDescription": result,
                      "description": "3", "speed": 4, "actions": ["wait"]}

        vitgity = Sources.Vitgities.Vitgity.Vitgity(dictionary)
        assert vitgity.getUp() == result


class TestIntroduce(unittest.TestCase):
    def testSuccess(self):
        result = "Some information"
        dictionary = {"name": "1", "startDescription": "2", "description": result,
                      "speed": 4, "actions": ["wait"]}

        vitgity = Sources.Vitgities.Vitgity.Vitgity(dictionary)
        assert vitgity.introduce() == result


class TestWait(unittest.TestCase):
    def testSuccess(self):
        dictionary = {"name": "1", "startDescription": "2", "description": "3", "speed": 4, "actions": ["wait"]}

        vitgity = Sources.Vitgities.Vitgity.Vitgity(dictionary)
        assert vitgity.wait() == ""
