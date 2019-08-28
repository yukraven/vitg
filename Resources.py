import random


def getRandFromArray(array):
    """ Returns a random index from an array of probabilities """
    temp = 0
    resultArray = []
    for i in array:
        temp += i
        resultArray.append(temp)             # Converting of the array into a form convenient for calculation
    randomValue = random.randint(1, 100)
    for i in range(len(resultArray)):
        if randomValue <= resultArray[i]:
            return i


getModByIndex = {
    "0": -30,
    "1": -20,
    "2": -10,
    "3": 0,
    "4": 10,
    "5": 20,
    "6": 30
}


class Resource:
    """ Base class for all objects in the game """
    startDescription = ""                   # Description that used to represent the object for the first time
    description = ""                        # Current description that storing the state of the object
    expectedCommands = []                   # Commands that should affect the object

    def __init__(self, startDescription, description, expectedCommands):
        """ Initialization """
        self.startDescription = startDescription
        self.description = description
        self.expectedCommands = expectedCommands

    def __repr__(self):
        """ Returns string information about the all properties of object """
        result = self.startDescription
        result += " | " + self.description
        result += " | Commands:"
        for i in self.expectedCommands:
            result += " "
            result += i
        return result

    def __str__(self):
        """ Returns current description """
        return self.description

    def getHi(self):
        """ Returns initial description """
        return self.startDescription


class Location(Resource):
    # Current weather, can change every turn
    weather = {"downfall": 0,               # 0 - clear, 1 - rain, 2 - hail, 3 - snow
               "wind": 0,                   # from 0 to 100
               "wet": 0,                    # from 0 to 100
               "temperature": 0,            # from 0 to 100
               "thunder": False}            # does thunder sound in the current turn
    # Arrays of probabilities
    weatherChances = {"downfall": {"0": [100, 0, 0, 0],                 # transitions 0->0, 0->1, 0->2, 0->3
                                   "1": [0, 100, 0, 0],                 # transitions 1->0, 1->1, 1->2, 1->3
                                   "2": [0, 0, 100, 0],                 # transitions 2->0, 2->1, 2->2, 2->3
                                   "3": [0, 0, 0, 100]},                # transitions 3->0, 3->1, 3->2, 3->3
                      "wind": {"0": [0, 0, 0, 100, 0, 0, 0]},           # mod -30, -20, -10, 0, +10, +20, +30
                      "wet": {"0": [0, 0, 0, 100, 0, 0, 0]},            # mod -30, -20, -10, 0, +10, +20, +30
                      "temperature": {"0": [0, 0, 0, 100, 0, 0, 0]},    # mod -30, -20, -10, 0, +10, +20, +30
                      "thunder": 30}        # Probability of thunder in one turn
    weatherChanging = {"downfall": {"0": ["", "", "", ""],
                                    "1": ["", "", "", ""],
                                    "2": ["", "", "", ""],
                                    "3": ["", "", "", ""]},
                       "wind": {"0": "", "1": "", "2": "",
                                "3": "",
                                "4": "", "5": "", "6": ""}}             # string messages for transitions

    def __init__(self, startDescription, description, expectedCommands, weather, weatherChances, weatherChanging):
        """ Initialization """
        Resource.__init__(self, startDescription, description, expectedCommands)
        self.weather = weather
        self.weatherChances = weatherChances
        self.weatherChanging = weatherChanging

    def __repr__(self):
        """ Complements the information by adding about weather and weather chances """
        result = Resource.__repr__(self)
        result += " | Weather:"
        for i in self.weather:
            result += " "
            result += str(self.weather[i])
        result += " | Weather chances:"
        for i in self.weatherChances:
            result += " "
            result += str(self.weatherChances[i])
        return result

    def __call__(self):
        """ Makes a turn, changes its condition, mostly weather, returns string information about it, else - "" """
        result = ""
        result += self._changeDownfall()
        result += self._changeAtmosphere("wind")
        result += self._changeAtmosphere("wet")
        result += self._changeAtmosphere("temperature")
        return result

    def _changeDownfall(self):
        """ Changes downfall, returns string information, if changed, else - "" """
        chances = self.weatherChances["downfall"]
        for state in chances:
            if self.weather["downfall"] == int(state):
                newDownfall = getRandFromArray(chances[state])
                if self.weather["downfall"] == newDownfall:             # if nothing changed
                    return ""
                oldDownfall = self.weather["downfall"]
                self.weather["downfall"] = newDownfall
                return self.weatherChanging["downfall"][str(oldDownfall)][newDownfall]

    def _changeAtmosphere(self, element):
        """ Changes wind, wet or temperature, if changed returns string information, else - "" """
        chances = self.weatherChances[element]
        curState = self.weather[element]
        for state in chances:
            if curState >= int(state):
                indexOfMod = getRandFromArray(chances[state])
                result = self.weatherChanging[element][str(indexOfMod)]
                curState += getModByIndex[str(indexOfMod)]
                if curState < 0:
                    curState = 0
                    result = ""
                elif curState > 100:
                    curState = 100
                    result = ""
                self.weather[element] = curState
                return result
