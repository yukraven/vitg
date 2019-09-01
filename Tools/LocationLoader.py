import json
import random
from Resources.Location import Location

class LocationLoader:

    jsonFile = ""
    locationsNames = []
    unusedLocationsNames = []

    def __init__(self, jsonFile):
        self.jsonFile = jsonFile
        with open(jsonFile, "r") as readFile:
            data = json.load(readFile)
            readFile.close()
        if data:
            for name in data:
                self.locationsNames.append(name)
            self.unusedLocationsNames = self.locationsNames.copy()

    def getNextRandomLocation(self):

        randomValue = random.randint(0, len(self.unusedLocationsNames))
        randomName = self.unusedLocationsNames[randomValue]
        with open(self.jsonFile, "r") as readFile:
            data = json.load(readFile)
            readFile.close()
        jsonLocation = data[randomName]
        self.unusedLocationsNames.зщз()
        return self.parseJsonLocation(jsonLocation, randomName)


    def parseJsonLocation(self, jsonLocation):
        dictResource = {
            "name":
        }