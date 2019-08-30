from Tools.Instruments import getRandFromArray
from Resources.Resource import Resource


class Location(Resource):
    # Current weather, can change every turn
    dFall = 0  # 0 - clear, 1 - rain, 2 - hail, 3 - snow
    wind = 0  # from 0 to 100 (1 points = 1 km/s)
    wet = 0  # from 0 to 100 (%)
    temperature = 0  # from 0 to 100 (1 point = 2 degrees Celsius, 50 = 0)
    thunder = False  # does thunder sound in the current turn

    # Arrays of probabilities to change downfall
    toChangeDFall = [[100, 0, 0, 0],  # transitions 0->0, 0->1, 0->2, 0->3
                     [0, 100, 0, 0],  # transitions 1->0, 1->1, 1->2, 1->3
                     [0, 0, 100, 0],  # transitions 2->0, 2->1, 2->2, 2->3
                     [0, 0, 0, 100]],  # transitions 3->0, 3->1, 3->2, 3->3
    temperatureFromWhich = {"rainFreezes": 0,
                            "rainEvaporates": 100,
                            "snowMelts": 100,
                            "hailMelts": 100},  # Temperature affecting downfall
    # Arrays of probabilities to change wind, wet and temperature
    toChangeWind = {0: [0, 0, 0, 100, 0, 0, 0]}  # mod -30, -20, -10, 0, +10, +20, +30
    toChangeWet = {0: [0, 0, 0, 100, 0, 0, 0]}  # mod -30, -20, -10, 0, +10, +20, +30
    toChangeTemperature = {0: [0, 0, 0, 100, 0, 0, 0]}  # mod -30, -20, -10, 0, +10, +20, +30
    # Probabilities of thunder in one turn depending on the downfall
    toThunder = [{"probability": 0, "wind": 0, "wet": 0, "temperature": 0},
                 {"probability": 0, "wind": 0, "wet": 0, "temperature": 0},
                 {"probability": 0, "wind": 0, "wet": 0, "temperature": 0},
                 {"probability": 0, "wind": 0, "wet": 0, "temperature": 0}]  # Probability under conditions

    # String data, that returns after changing (AC) properties
    ACdFall = [["", "", "", ""],
               ["", "", "", ""],
               ["", "", "", ""],
               ["", "", "", ""]]  # After changing downfall
    ACwind = ["", "", "", "", "", "", ""]  # After changing wind
    ACwet = ["", "", "", "", "", "", ""]  # After changing wet
    ACtemperature = ["", "", "", "", "", "", ""]  # After changing temperature
    ACthunder = ""  # After thunder!!!

    def __init__(self, dictResource, dictLocation):
        """ Initialization """
        Resource.__init__(self, dictResource)

        self.dFall = dictLocation["dFall"]
        self.wind = dictLocation["wind"]
        self.wet = dictLocation["wet"]
        self.temperature = dictLocation["temperature"]
        self.thunder = dictLocation["thunder"]

        self.toChangeDFall = dictLocation["toChangeDFall"]
        self.temperatureFromWhich = dictLocation["temperatureFromWhich"]
        self.toChangeWind = dictLocation["toChangeWind"]
        self.toChangeWet = dictLocation["toChangeWet"]
        self.toChangeTemperature = dictLocation["toChangeTemperature"]
        self.toThunder = dictLocation["toThunder"]

        self.ACdFall = dictLocation["ACdFall"]
        self.ACwind = dictLocation["ACwind"]
        self.ACwet = dictLocation["ACwet"]
        self.ACtemperature = dictLocation["ACtemperature"]
        self.ACthunder = dictLocation["ACthunder"]

    def __repr__(self):
        """ Complements the information by adding about weather and weather chances """
        result = Resource.__repr__(self) + " | "

        result += str(self.dFall) + " " + str(self.wind) + " " + str(self.wet) + " " + \
                  str(self.temperature) + " " + str(self.thunder) + " "

        result += str(self.toChangeDFall) + " " + str(self.temperatureFromWhich) + " " + \
                  str(self.toChangeWind) + " " + str(self.toChangeWet) + " " + \
                  str(self.toChangeTemperature) + " " + self.toThunder + " "

        return result

    def __call__(self):
        """ Makes a turn, changes its condition, mostly weather, returns string information about it, else - "" """
        result = self.changeDFall()
        result += self._changeAtmosphere("wind", "random")
        result += self._changeAtmosphere("wet", "random")
        result += self._changeAtmosphere("temperature", "random")
        result += self._getThunder()
        return result

    def changeDFall(self):
        """ Changes downfall, returns string information, if changed, else - "" """
        for index in range(len(self.toChangeDFall)):
            if self.dFall == index:
                newDFall = self.tryChangeDFall[getRandFromArray(self.toChangeDFall[index])]()
                if self.dFall == newDFall:  # if nothing changed
                    return ""
                oldDFall, self.dFall = self.dFall, newDFall
                return self.ACdFall[oldDFall][newDFall]

    def changeWind(self, index):
        """ Changes wind, if changed returns string information, else - "" """
        curWind = self.wind
        for wind in self.toChangeWind:
            if curWind > wind:
                indexOfMod, mod = self.getIndexAndMod(self.toChangeWind[wind], index)
                result = self.ACwind[indexOfMod]
                curWind += mod
                if curWind < 0: curWind = 0
                elif curWind > 100: curWind = 100
                self.wind = curWind
                return result
        return ""
"......................................................................................................................"
    def getIndexAndMod(self, array, index):
        if index == "random":
            indexOfMod = getRandFromArray(array)
        else:
            indexOfMod = index
        mod = self.getModByIndex[indexOfMod]
        return indexOfMod, mod

    def changeAtmosphere(self, element, value):
        """ Changes wind, wet or temperature, if changed returns string information, else - "" """
        curValue = self.
        for state in self.toChangeElement[element]:
            if curState >= int(state):
                if index == "random":
                    indexOfMod = getRandFromArray(chances[state])
                else:
                    indexOfMod = index
                result = self._weatherChanging[element][str(indexOfMod)]
                curState += self.getModByIndex[indexOfMod]
                if curState < 0:
                    curState = 0
                    result = ""
                elif curState > 100:
                    curState = 100
                    result = ""
                self._weather[element] = curState
                return result

    def _getThunder(self):
        """ Adds sound of thunder or not """
        self._weather["thunder"] = False
        chances = self._weatherChances["thunder"][str(self._weather["downfall"])]
        prob = chances["probability"]
        if prob > 0:
            for i in ["wind", "wet", "temperature"]:
                if self._weather[i] < chances[i]:
                    return ""
            if getRandFromArray([prob, 100 - prob]) == 0:
                self._weather["thunder"] = True
                return self._weatherChanging["thunder"]
        return ""

    def _tryRain(self):
        """ Try change downfall for rain, changes wet, return new state """
        temperatureFor = self._weatherChances["tempAndDownfall"]
        temperature = self._weather["temperature"]
        if temperature <= temperatureFor["rainFreezes"]:
            newState = self._tryHail()
        elif temperature >= temperatureFor["rainEvaporates"]:
            self._changeAtmosphere("wet", 6)  # +30
            newState = 0  # Clear
        else:
            self._changeAtmosphere("wet", 6)  # +30
            newState = 1  # Rain
        return newState

    def _tryHail(self):
        """ Try change downfall for hail, changes temperature, return new state """
        temperatureFor = self._weatherChances["tempAndDownfall"]
        temperature = self._weather["temperature"]
        if temperature >= temperatureFor["hailMelts"]:
            newState = self._tryRain()
        else:
            self._changeAtmosphere("temperature", 2)  # -10
            newState = 2  # Hail
        return newState

    def _trySnow(self):
        """ Try change downfall for snow, changes temperature, return new state """
        temperatureFor = self._weatherChances["tempAndDownfall"]
        temperature = self._weather["temperature"]
        if temperature >= temperatureFor["snowMelts"]:
            newState = self._tryRain()
        else:
            self._changeAtmosphere("temperature", 2)  # -10
            newState = 3  # Snow
        return newState

    getModByIndex = {
        0: -30,
        1: -20,
        2: -10,
        3: 0,
        4: 10,
        5: 20,
        6: 30
    }  # For arrays of probabilities for wind, wet and temperature

    tryChangeDFall = {
        0: lambda self: 0,
        1: tryRain,
        2: tryHail,
        3: trySnow
    }   # Switch for index - "try" method


