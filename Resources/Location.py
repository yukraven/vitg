from Instruments import getRandFromArray
from Resources.Resource import Resource


class Location(Resource):
    # Current weather, can change every turn
    weather = {"downfall": 0,               # 0 - clear, 1 - rain, 2 - hail, 3 - snow
               "wind": 0,                   # from 0 to 100 (1 points = 1 km/s)
               "wet": 0,                    # from 0 to 100 (%)
               "temperature": 0,            # from 0 to 100 (1 point = 2 degrees Celsius, 50 = 0)
               "thunder": False}            # does thunder sound in the current turn
    # Arrays of probabilities
    weatherChances = {"downfall": {"0": [100, 0, 0, 0],                 # transitions 0->0, 0->1, 0->2, 0->3
                                   "1": [0, 100, 0, 0],                 # transitions 1->0, 1->1, 1->2, 1->3
                                   "2": [0, 0, 100, 0],                 # transitions 2->0, 2->1, 2->2, 2->3
                                   "3": [0, 0, 0, 100]},                # transitions 3->0, 3->1, 3->2, 3->3
                      "tempAndDownfall": {"rainFreezes": 45,
                                          "rainEvaporates": 80,
                                          "snowMelts": 55,
                                          "hailMelts": 60},             # Temperature affecting downfall
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
        result += self._changeAtmosphere("wind", "random")
        result += self._changeAtmosphere("wet", "random")
        result += self._changeAtmosphere("temperature", "random")
        return result

    def _changeDownfall(self):
        """ Changes downfall, returns string information, if changed, else - "" """
        chances = self.weatherChances["downfall"]
        for state in chances:
            if self.weather["downfall"] == int(state):
                newDownfall = self._tryChangeDownfall[getRandFromArray(chances[state])](self)
                if self.weather["downfall"] == newDownfall:             # if nothing changed
                    return ""
                oldDownfall = self.weather["downfall"]
                self.weather["downfall"] = newDownfall
                return self.weatherChanging["downfall"][str(oldDownfall)][newDownfall]

    def _changeAtmosphere(self, element, index):
        """ Changes wind, wet or temperature, if changed returns string information, else - "" """
        chances = self.weatherChances[element]
        curState = self.weather[element]
        for state in chances:
            if curState >= int(state):
                if index == "random":
                    indexOfMod = getRandFromArray(chances[state])
                else:
                    indexOfMod = index
                result = self.weatherChanging[element][str(indexOfMod)]
                curState += self.getModByIndex[indexOfMod]
                if curState < 0:
                    curState = 0
                    result = ""
                elif curState > 100:
                    curState = 100
                    result = ""
                self.weather[element] = curState
                return result

    def _tryRain(self):
        """ Try change downfall for rain, changes wet, return new state """
        temperatureFor = self.weatherChances["tempAndDownfall"]
        temperature = self.weather["temperature"]
        if temperature <= temperatureFor["rainFreezes"]:
            newState = self._tryHail()
        elif temperature >= temperatureFor["rainEvaporates"]:
            self._changeAtmosphere("wet", 6)                            # +30
            newState = 0                    # Clear
        else:
            self._changeAtmosphere("wet", 6)                            # +30
            newState = 1                    # Rain
        return newState

    def _tryHail(self):
        """ Try change downfall for hail, changes temperature, return new state """
        temperatureFor = self.weatherChances["tempAndDownfall"]
        temperature = self.weather["temperature"]
        if temperature >= temperatureFor["hailMelts"]:
            newState = self._tryRain()
        else:
            self._changeAtmosphere("temperature", 2)                    # -10
            newState = 2                    # Hail
        return newState

    def _trySnow(self):
        """ Try change downfall for snow, changes temperature, return new state """
        temperatureFor = self.weatherChances["tempAndDownfall"]
        temperature = self.weather["temperature"]
        if temperature >= temperatureFor["snowMelts"]:
            newState = self._tryRain()
        else:
            self._changeAtmosphere("temperature", 2)                    # -10
            newState = 3                    # Snow
        return newState

    getModByIndex = {
        0: -30,
        1: -20,
        2: -10,
        3: 0,
        4: 10,
        5: 20,
        6: 30
    }                                       # For arrays of probabilities for wind, wet and temperature

    _tryChangeDownfall = {
        0: lambda self: 0,
        1: _tryRain,
        2: _tryHail,
        3: _trySnow
    }                                       # Switch for index - "try" method