import logging
import Sources.Hero
import Sources.Parser

log = logging.getLogger("gamemaster")


class GameMaster:

    current_heroes = {}

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
        log.info("получаем героя")
        user_id = str(user_id)
        if user_id in self.current_heroes:
            hero = self.current_heroes[user_id]
        else:
            log.info("id игрока нет в базе, создаем нового героя")
            hero = self.createHero(user_id)
        return hero

    def createHero(self, user_id):
        hero = Sources.Hero.Hero()
        self.current_heroes[str(user_id)] = hero
        return hero
