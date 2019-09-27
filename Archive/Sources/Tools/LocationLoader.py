import json
import random
from Archive.Sources.Resources.Location import Location


class LocationLoader:

    jsonFiles = []
    locationsNames = [[]]
    unusedLocationsNames = [[]]

    def __init__(self, jsonFiles):
        self.jsonFiles = jsonFiles
        self.locationsNames = []
        self.unusedLocationsNames = []
        index = 0
        for jsonFile in self.jsonFiles:
            self.locationsNames.append([])
            with open(jsonFile, "r") as readFile:
                data = json.load(readFile)
                readFile.close()
            if data:
                for name in data:
                    self.locationsNames[index].append(name)
            index += 1
        self.unusedLocationsNames = self.locationsNames.copy()

    def getRandomLocation(self):
        randomJsonNumber = random.randint(0, len(self.jsonFiles)-1)
        jsonPath = self.jsonFiles[randomJsonNumber]
        randomLocationNumber = random.randint(0, len(self.locationsNames[randomJsonNumber])-1)
        locationName = self.locationsNames[randomJsonNumber][randomLocationNumber]
        return self.createLocation(jsonPath, locationName)

    def getNextRandomLocation(self):
        locationName = ""
        jsonPath = ""
        while locationName == "":
            randomJsonNumber = random.randint(0, len(self.jsonFiles)-1)
            jsonPath = self.jsonFiles[randomJsonNumber]
            if len(self.unusedLocationsNames[randomJsonNumber]) > 0:
                randomLocationNumber = random.randint(0, len(self.unusedLocationsNames[randomJsonNumber])-1)
                locationName = self.unusedLocationsNames[randomJsonNumber][randomLocationNumber]
                self.unusedLocationsNames[randomJsonNumber].pop(randomLocationNumber)
        return self.createLocation(jsonPath, locationName)

    def createLocation(self, jsonPath, locationName):
        with open(jsonPath, "r") as readFile:
            data = json.load(readFile)
            readFile.close()
        jsonLocation = data[locationName]
        dictResource = {"name": locationName, **jsonLocation["dictResource"]}
        dictLocation = jsonLocation["dictLocation"]
        location = Location(dictResource, dictLocation)
        return location
