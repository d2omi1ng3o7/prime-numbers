import math


def is_prime(number):
    if number <= 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def howPrimeNumbers(name, diogonal):
    quantityPrimeNumbers = 0

    for number in diogonal:
        if is_prime(number):
            quantityPrimeNumbers += 1

    return name, quantityPrimeNumbers


print(howPrimeNumbers('2-6:6-2', [12, 2, 5, 8, 23, 26]))