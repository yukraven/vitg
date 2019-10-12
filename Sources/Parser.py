class Parser:
    sylls = [{u"би": "attack"},
             {u"люб": "love"}]
    maxSyll = 3

    def encode(self, word):
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
        listOfWords = self.getListOfWords(message)
        result = []
        for word in listOfWords:
            result.append(self.encode(word))
        return result

    def getListOfWords(self, message):
        listWithoutSpaces = message.split(" ")
        result = []
        for word in listWithoutSpaces:
            word = word.lower()
            if word.isalnum():
                result.append(word)
            else:
                tempList = self.splitByMarks(word)
                for tempWord in tempList:
                    result.append(tempWord)
        return result

    def splitByMarks(self, wordWithMarks):
        marks = [".", ",", "!", "?"]
        words = [wordWithMarks]
        for mark in marks:
            tempWords = []
            for word in words:
                if word.count(mark) > 0:
                    tempWords += word.split(mark)
                elif word != "":
                    tempWords += [word]
            words = tempWords

        return words
