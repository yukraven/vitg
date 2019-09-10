import random
from Sources.Tools.Exceptions import ValueIsNotProbabilityError
from Sources.Tools.Exceptions import SumOfProbabilitiesIsNot100Error


def getRandFromArray(array, withWhat):
    """ Returns a random index from an array of probabilities """
    if type(array) is not list:
        raise TypeError
    if len(array) == 0:
        raise ValueError

    if withWhat == "withProbs":
        for i in array:
            if not (isinstance(i, int) or isinstance(i, float)):
                raise ValueError
        for i in array:
            if i < 0 or i > 100:
                raise ValueIsNotProbabilityError(i)
        sumOfProbabilities = 0
        for i in array:
            sumOfProbabilities += i
        if sumOfProbabilities != 100:
            raise SumOfProbabilitiesIsNot100Error

        temp = 0
        resultArray = []
        for i in array:
            temp += i
            resultArray.append(temp)             # Converting of the array into a form convenient for calculation
        randomValue = random.randint(1, 100)
        for i in range(len(resultArray)):
            if randomValue <= resultArray[i]:
                return i

    if withWhat == "withValues":
        randomValue = random.randint(0, len(array) - 1)
        return array[randomValue]
