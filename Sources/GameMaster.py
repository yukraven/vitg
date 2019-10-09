import Sources.Parser


class GameMaster:

    currentHeroes = {"441591973": "hero"}

    def sendMessage(self, message, userID):
        if str(userID) in self.currentHeroes:
            currentHero = self.currentHeroes[str(userID)]
        else:
            return "Герой не задан"
        print(message)
        words = message.split(" ")
        print(words)
        parser = Sources.Parser.Parser()
        actions = []
        for word in words:
            print(word)
            print(parser.getCommand(word))
            actions.append(parser.getCommand(word))
        print(actions)
        result = ""
        for action in actions:
            if isinstance(action, str):
                result += " "
                result += action
        if result != "":
            return result
        else:
            return "Нет ответа"