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
        result += " | "
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
