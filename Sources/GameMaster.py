import Sources.Parser


class GameMaster:

    current_heroes = {"441591973": "hero"}

    def sendMessage(self, message, user_id):
        hero = self.getHero(user_id)
        parser = Sources.Parser.Parser()
        actions = parser.getActions(message)

        result = ""
        for action in actions:
            if isinstance(action, str):
                result += " "
                result += action
        if result != "":
            return result
        else:
            return "Нет ответа"

    def getHero(self, user_id):
        user_id = str(user_id)
        if user_id in self.current_heroes:
            hero = self.current_heroes[user_id]
        else:
            hero = self.createHero(user_id)
        return hero

    def createHero(self, user_id):
        return ""
