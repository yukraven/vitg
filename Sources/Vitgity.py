class Vitgity:
    """ Base class for all objects in the game """
    name = "None"               # Unique identifier of the object
    startDescription = "None"   # Start message, that prints, when object is getting up on the stage
    description = "None"        # Message, describing the object, that prints on introduce() call

    speed = 0                   # It defines, how much earlier the object can speech

    actions = {}                # List of actions, which the object can do

    def __init__(self, dictionary):
        """ Initialization """
        try:
            for i in ["name", "startDescription", "description", "speed"]:
                if i == "speed" and type(dictionary[i] == int) or type(dictionary) == str:
                    pass
                else:
                    raise TypeError("Bad type of %s" % i)

            self.name = dictionary["name"]
            self.startDescription = dictionary["startDescription"]
            self.description = dictionary["description"]
            self.speed = dictionary["speed"]

            for action in dictionary["actions"]:
                if action == "wait":
                    self.
        except (AttributeError, TypeError) as exception:
            self.name = "ErrorLoad"
            self.description = exception

            pass

    def getUp(self):
        """ To get up on the stage. Returns startDescription """
        return self.startDescription

    def introduce(self):
        """ To introduce yourself. Returns description """
        return self.description

    def speech(self):
        """ To make a turn. Returns the result of turn """
        return self.wait()

    def wait(self):
        """ Just wait. Do nothing """
        return ""
