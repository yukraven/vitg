import json
import random
from Resources.Location import Location


class LocationLoader:

    jsonFiles = []
    locationsNames = [[]]
    unusedLocationsNames = [[]]

    def __init__(self, jsonFiles):
        self.jsonFiles = jsonFiles
        ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        with open(jsonFiles, "r") as readFile:
            data = json.load(readFile)
            readFile.close()
        if data:
            for name in data:
                self.locationsNames.append(name)
            self.unusedLocationsNames = self.locationsNames.copy()

    def getRandomLocation(self):
        randomJsonNumber = random.randint(0, len(self.jsonFiles))
        jsonPath = self.jsonFiles[randomJsonNumber]
        randomLocationNumber = random.randint(0, len(self.locationsNames[randomJsonNumber]))
        locationName = self.locationsNames[randomLocationNumber]
        return self.createLocationByName(jsonPath, locationName)

    def getNextRandomLocation(self):
        locationName = ""
        jsonPath = ""
        while locationName == "":
            randomJsonNumber = random.randint(0, len(self.jsonFiles))
            jsonPath = self.jsonFiles[randomJsonNumber]
            if len(self.unusedLocationsNames[randomJsonNumber]) > 0:
                randomLocationNumber = random.randint(0, len(self.unusedLocationsNames[randomJsonNumber]))
                locationName = self.unusedLocationsNames[randomLocationNumber]
                self.unusedLocationsNames[randomJsonNumber].pop(randomLocationNumber)
        return self.createLocationByName(jsonPath, locationName)

    def createLocationByName(self, jsonPath, locationName):
        with open(jsonPath, "r") as readFile:
            data = json.load(readFile)
            readFile.close()
        jsonLocation = data[locationName]
        dictResource = {"name": locationName, **jsonLocation["dictResource"]}
        dictLocation = jsonLocation["dictLocation"]
        location = Location(dictResource, dictLocation)
        return location
