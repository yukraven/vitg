import random


def getRandFromArray(array):
    """ Returns a random index from an array of probabilities """
    temp = 0
    resultArray = []
    for i in array:
        temp += i
        resultArray.append(temp)             # Converting of the array into a form convenient for calculation
    randomValue = random.randint(1, 100)
    for i in range(len(resultArray)):
        if randomValue <= resultArray[i]:
            return i
