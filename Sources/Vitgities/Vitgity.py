import logging

log = logging.getLogger("vitgity")


class Vitgity:
    """ Base class for all objects in the game """
    name = "None"               # Unique identifier of the object
    startDescription = "None"   # Start message, that prints, when object is getting up on the stage
    description = "None"        # Message, describing the object, that prints on introduce() call

    speed = 0                   # It defines, how much earlier the object can speech

    actions = {}                # List of actions, which the object can do

    def __init__(self, dictionary):
        """ Initialization """
        log.info("initialization")
        try:
            for i in ["name", "startDescription", "description", "speed"]:
                log.debug(i)
                if i == "speed" and type(dictionary[i]) == int or not i == "speed" and type(dictionary[i]) == str:
                    pass
                else:
                    log.error("loading error - (name, startDescription, description, speed)")
                    raise TypeError

            self.name = dictionary["name"]
            log.debug(self.name)
            self.startDescription = dictionary["startDescription"]
            log.debug(self.startDescription)
            self.description = dictionary["description"]
            log.debug(self.description)
            self.speed = dictionary["speed"]
            log.debug(self.speed)

            for action in dictionary["actions"]:
                log.debug(action)
                if type(action) != str:
                    log.error("loading error - actions")
                    raise TypeError
            self.actions = dictionary["actions"]

        except (KeyError, TypeError):
            log.error("got exception")
            self.name = "ErrorLoad"

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
