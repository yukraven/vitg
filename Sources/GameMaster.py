import logging
import Sources.Vitgities.Hero
import Sources.Parser

log = logging.getLogger("gamemaster")


class GameMaster:

    current_heroes = {}
    current_scenes = {}

    def sendMessage(self, message, user_id):
        scene = self.getScene(user_id)
        parser = Sources.Parser.Parser()
        actions = parser.getActions(message)

        return scene.sendMessage(actions)

    def getScene(self, user_id):
        log.info("получаем сцену")
        user_id = str(user_id)
        if user_id in self.current_scenes:
            return self.current_scenes[user_id]
        else:
            log.info("для id игрока не создано ни одной сцены, создаем новую на основе его героя")
            if user_id not in self.current_heroes:
                log.info("по какой то причине для id игрока не сохранено героя, создадим нового")
                self.createHero(user_id)
            return self.createScene(self.current_heroes[user_id])

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
        hero = Sources.Vitgities.Hero.Hero()
        self.current_heroes[str(user_id)] = hero
        return hero

    def createScene(self, hero):
        pass
