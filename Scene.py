class Scene:
    """ The main class of a gameplay, stores the whole information about current location, props and actors """
    _location = ""
    _props = []
    _actors = []
    _player = ""

    def __init__(self, location, props, actors, player):
        self._location = location
        self._props = props
        self._actors = actors
        self._player = player

    def __repr__(self):
        result = self._location.name
        for i in self._props:
            result += " " + i.name
        for i in self._actors:
            result += " " + i.name
        return result

    def __call__(self):
        self._location()

    def command(self, commands):
        for i in commands:
            if i in self._location.expectedCommands:
                self._location.command(i, commands[i])