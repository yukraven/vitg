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
                            "hailMelts": 100,
                            "snowMelts": 100},  # Temperature affecting downfall
    # Arrays of probabilities to change wind, wet and temperature
    toChangeWind = {"0": [0, 0, 0, 100, 0, 0, 0]}  # mod -30, -20, -10, 0, +10, +20, +30
    toChangeWet = {"0": [0, 0, 0, 100, 0, 0, 0]}  # mod -30, -20, -10, 0, +10, +20, +30
    toChangeTemperature = {"0": [0, 0, 0, 100, 0, 0, 0]}  # mod -30, -20, -10, 0, +10, +20, +30
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

    def __init__(self, dictResource=None, dictLocation=None):
        """ Initialization """
        Resource.__init__(self, dictResource)
        try:
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
        except TypeError:
            pass

    def __repr__(self):
        """ Complements the information by adding about weather and weather chances """
        result = Resource.__repr__(self) + " | "

        result += str(self.dFall) + " " + str(self.wind) + " " + str(self.wet) + " " + \
                  str(self.temperature) + " " + str(self.thunder) + " "

        result += str(self.toChangeDFall) + " " + str(self.temperatureFromWhich) + " " + \
                  str(self.toChangeWind) + " " + str(self.toChangeWet) + " " + \
                  str(self.toChangeTemperature) + " " + str(self.toThunder) + " "

        return result

    def __str__(self):
        return Resource.__str__(self)

    def __call__(self):
        """ Makes a turn, changes its condition, mostly weather, returns string information about it, else - "" """
        result = self.changeDFall()
        result += self.changeWind("random")
        result += self.changeWet("random")
        result += self.changeTemperature("random")
        result += self.getThunder()
        return result

    def changeDFall(self):
        """ Changes downfall, returns string information, if changed, else - "" """
        for index in range(len(self.toChangeDFall)):
            if self.dFall == index:
                newDFall = self.tryChangeDFall[getRandFromArray(self.toChangeDFall[index])](self)
                if self.dFall == newDFall:  # if nothing changed
                    return ""
                oldDFall, self.dFall = self.dFall, newDFall
                return self.ACdFall[oldDFall][newDFall]

    def changeWind(self, index):
        """ Changes wind, if changed returns string information, else - "" """
        curWind = self.wind
        for wind in self.toChangeWind:
            wind = int(wind)
            if curWind >= wind:
                indexOfMod, mod = self.getIndexAndMod(self.toChangeWind[str(wind)], index)
                result = self.ACwind[indexOfMod]
                curWind += mod
                if curWind < 0: curWind = 0
                elif curWind > 100: curWind = 100
                self.wind = curWind
                return result
        return ""

    def changeWet(self, index):
        """ Changes wet, if changed returns string information, else - "" """
        curWet = self.wet
        for wet in self.toChangeWet:
            wet = int(wet)
            if curWet >= wet:
                indexOfMod, mod = self.getIndexAndMod(self.toChangeWet[str(wet)], index)
                result = self.ACwet[indexOfMod]
                curWet += mod
                if curWet < 0: curWet = 0
                elif curWet > 100: curWet = 100
                self.wet = curWet
                return result
        return ""

    def changeTemperature(self, index):
        """ Changes temperature, if changed returns string information, else - "" """
        curTemperature = self.temperature
        for temperature in self.toChangeTemperature:
            temperature = int(temperature)
            if curTemperature >= temperature:
                indexOfMod, mod = self.getIndexAndMod(self.toChangeTemperature[str(temperature)], index)
                result = self.ACtemperature[indexOfMod]
                curTemperature += mod
                if curTemperature < 0: curTemperature = 0
                elif curTemperature > 100: curTemperature = 100
                self.temperature = curTemperature
                return result
        return ""

    def getIndexAndMod(self, array, index):
        if index == "random":
            indexOfMod = getRandFromArray(array)
        else:
            indexOfMod = index
        mod = self.getModByIndex[indexOfMod]
        return indexOfMod, mod

    def getThunder(self):
        """ Adds sound of thunder or not """
        self.thunder = False
        chances = self.toThunder[self.dFall]
        prob = chances["probability"]
        if prob > 0:
            if self.wind < chances["wind"] or self.wet < chances["wet"] or self.temperature < chances["temperature"]:
                return ""
            if getRandFromArray([prob, 100 - prob]) == 0:
                self.thunder = True
                return self.ACthunder
        return ""

    def tryRain(self):
        """ Try change downfall for rain, changes wet, return new state """
        if self.temperature <= self.temperatureFromWhich["rainFreezes"]:
            newState = self.tryHail()
        elif self.temperature >= self.temperatureFromWhich["rainEvaporates"]:
            self.changeWet(6)  # +30
            newState = 0  # Clear
        else:
            self.changeWet(6)  # +30
            newState = 1  # Rain
        return newState

    def tryHail(self):
        """ Try change downfall for hail, changes temperature, return new state """
        if self.temperature >= self.temperatureFromWhich["hailMelts"]:
            newState = self.tryRain()
        else:
            self.changeTemperature(2)  # -10
            newState = 2  # Hail

        return newState

    def trySnow(self):
        """ Try change downfall for snow, changes temperature, return new state """
        if self.temperature >= self.temperatureFromWhich["snowMelts"]:
            newState = self.tryRain()
        else:
            self.changeTemperature(2)  # -10
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

    tryChangeDFall = [
        lambda self: 0,
        tryRain,
        tryHail,
        trySnow
    ]   # Switch for index - "try" method


