from Enums import Wthr

class Resource:
    __description = ""
    __expectedCommands = []

    def __init__(self, description, expectedCommands):
        self.__description = description
        self.__expectedCommands = expectedCommands

    def __repr__(self):
        result = self.__description
        result += " Commands:"
        for i in self.__expectedCommands:
            result += " "
            result += i
        return result
        
    def __str__(self):
        return self.__description

    def __call__(self):
        return self.__description

class Location:
    __weather = Wthr.clear

    def __init__(self, description, expectedCommands, weather):
        Resource.__init__(self, description, expectedCommands)
        self.__weather = weather

    def __repr__(self):
        result = Resource.__repr__(self)
        result += ". Weather: "
        result += str(self.__weather)
        return result

    def __str__(self):
        return Resource.__str__(self)

    def __call__(self):
        return Resource.__call__(self)
