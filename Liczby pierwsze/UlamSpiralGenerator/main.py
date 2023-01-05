import numpy as np
from math import ceil
import PIL as pillow


def ifPrimeNumber(num):
    for x in range(2, num//2+1):
        if num % x == 0:
            return False
    return True

def boardGenarator(x, y):
    ulamArray = np.zeros([x, y], dtype='int32')
    positionX = ceil(x/2)-1
    positionY = ceil(y/2)-1
    diretion = (0, 1), (-1, 0), (0, -1), (1, 0)
    diretionI = 0
    turn = 1
    turnI = turn
    turnB = True

    for i in range(1, x*y+1):
        ulamArray[positionX, positionY] = i
        if turnI == 0:
            if turnB:
                turnB = False
            else:
                turn += 1
                turnB = True
            turnI = turn
            diretionI += 1
            if diretionI == 4:
                diretionI = 0

        positionX, positionY = positionX + diretion[diretionI][0], positionY + diretion[diretionI][1]
        turnI -= 1

    
    return ulamArray

def findPrimeNumbers(ulamArray):
    positionsPrimeNumbers = []
    x, y = np.shape(ulamArray)[0], np.shape(ulamArray)[1]

    for i in range(x):
        for j in range(y):
            number = ulamArray[i, j]

            if ifPrimeNumber(number):
                positionsPrimeNumbers.append(f'{i}:{j}')
                
    return positionsPrimeNumbers

def printImage(ulamArray, positionsPrimeNumbers):
    pass

if __name__ == '__main__':
    ulamArray = boardGenarator(11, 11) # nie może być parzystych bo głupoty wychodzą
    # print(findPrimeNumbers(ulamArray))
    print(ulamArray)

    