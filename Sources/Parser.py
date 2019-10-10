class Parser:
    sylls = [{u"би": "attack"},
             {u"люб": "love"}]
    maxSyll = 3

    def getCommand(self, word):
        syllLength = len(word) if len(word) < self.maxSyll else self.maxSyll
        for i in range(syllLength, 1, -1):
            start = 0
            end = i
            currentSylls = self.sylls[i-2]
            while end <= len(word):
                key = word[start:end]
                try:
                    command = currentSylls[key]
                    return command
                except KeyError:
                    start += 1
                    end += 1

    def getActions(self, message):
        return ""