import random
from Tools.Exceptions import ValueIsNotProbabilityError


def getRandFromArray(array):
    """ Returns a random index from an array of probabilities """
    if type(array) is not list:
        raise TypeError
    if len(array) == 0:
        raise ValueError
    for i in array:
        if i < 0 or i > 100:
            raise ValueIsNotProbabilityError(i)

    temp = 0
    resultArray = []
    for i in array:
        temp += i
        resultArray.append(temp)             # Converting of the array into a form convenient for calculation
    randomValue = random.randint(1, 100)
    for i in range(len(resultArray)):
        if randomValue <= resultArray[i]:
            return i
