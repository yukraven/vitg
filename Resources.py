import random


def getRandFromMass(mass):
    temp = 0
    resultMass = []
    for i in mass:
        temp += i
        resultMass.append(temp)
    randomValue = random.randint(1, 100)
    for i in range(len(resultMass)):
        if randomValue <= resultMass[i]:
            return i


class Resource:
    startDescription = ""
    description = ""
    expectedCommands = []

    def __init__(self, startDescription, description, expectedCommands):
        self.startDescription = startDescription
        self.description = description
        self.expectedCommands = expectedCommands

    def __repr__(self):
        result = self.startDescription
        result += " | " + self.description
        result += " | Commands:"
        for i in self.expectedCommands:
            result += " "
            result += i
        return result

    def __str__(self):
        return self.description

    def getHi(self):
        return self.startDescription


class Location(Resource):
    weather = {}
    weatherChances = {}
    weatherChanging = {}

    def __init__(self, startDescription, description, expectedCommands, weather, weatherChances, weatherChanging):
        Resource.__init__(self, startDescription, description, expectedCommands)
        self.weather = weather
        self.weatherChances = weatherChances
        self.weatherChanging = weatherChanging

    def __repr__(self):
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
        result = ""
        result += self.__changeDownfall()
        return result

    def __changeDownfall(self):
        result = ""
        downfall = self.weatherChances["downfall"]
        for state in downfall:
            if self.weather["downfall"] == int(state):
                newDownfall = getRandFromMass(downfall[state]) + 1
                if self.weather["downfall"] == newDownfall:
                    return ""
                oldDownfall = self.weather["downfall"]
                self.weather["downfall"] = newDownfall
                return self.weatherChanging["downfall"][str(oldDownfall)][newDownfall - 1]
