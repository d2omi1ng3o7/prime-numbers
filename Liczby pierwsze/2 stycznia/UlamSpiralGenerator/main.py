import numpy as np
from math import ceil
import math


def is_prime(n):
    if n <= 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def boardGenarator(size):
    ulamArray = np.zeros([size, size], dtype='int64')
    x, y = size//2, size//2
    diretion = (0, 1), (-1, 0), (0, -1), (1, 0)
    diretionI = 0
    turn = 1
    turnI = turn
    turnB = True

    for i in range(1, size*size+1):
        ulamArray[x, y] = i
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

        x, y = x + diretion[diretionI][0], y + diretion[diretionI][1]
        turnI -= 1

    
    return ulamArray

def diagonals(array, size):
    diagonals = []
    diretion = [0, 0]
    for i in range(0, ceil(size/2)):
        diretion[0] += -1
        diretion[1] += 1
        diagonal = []
        for j in range(0, ceil(size/2)):
            diagonal.append(array[ceil(size/2)-1-j+diretion[0], j+diretion[1]])
        diagonals.append(diagonal)

    return diagonals


if __name__ == '__main__':
    
    size = 9
    ulamArray = boardGenarator(size)
    x = 0
    largest = ulamArray[size-1, size-1]
    largestLenght = int(len(str(largest)))

    diagonals = diagonals(ulamArray, size)

    for i in range(size):
        for j in range(size):

            number = ulamArray[i, j]
            numberLenght = int(len(str(number)))
            space = ' '*(largestLenght-numberLenght)

            if is_prime(number):
                print(f'{space}\033[91m', number, '\033[0m', end='')
            else:
                print(f'{space} {number} ', end='')

            x += 1
            if x == size:
                print()
                x = 0

    print(diagonals)


