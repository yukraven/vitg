from Enums import DFall


class Resource:
    __startDescription = ""
    __description = ""
    __expectedCommands = []

    def __init__(self, startDescription, description, expectedCommands):
        self.__startDescription = startDescription
        self.__description = description
        self.__expectedCommands = expectedCommands

    def __repr__(self):
        result = self.__startDescription
        result += " " + self.__description
        result += " Commands:"
        for i in self.__expectedCommands:
            result += " "
            result += i
        return result

    def __str__(self):
        return self.__description

    def getHi(self):
        return self.__startDescription


class Location:
    __weather = {}

    def __init__(self, description, expectedCommands, weather):
        Resource.__init__(self, description, expectedCommands)
        self.__weather = weather

    def __repr__(self):
        result = Resource.__repr__(self)
        # result += ". Weather: "
        # result += str(self.__weather)
        return result

    def __str__(self):
        return Resource.__str__(self)
