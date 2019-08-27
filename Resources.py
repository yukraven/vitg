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

    def __init__(self, startDescription, description, expectedCommands, weather, weatherChances):
        Resource.__init__(self, startDescription, description, expectedCommands)
        self.weather = weather
        self.weatherChances = weatherChances

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
        return True
