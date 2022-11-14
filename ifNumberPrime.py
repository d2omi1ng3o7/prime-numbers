
def ifNumberPrime(num):
    if num <= 1:
        return False

    for x in range(2, num // 2 + 1):
        if num % x == 0:
            return False

    return True

if __name__ == '__main__':
    print(ifNumberPrime(int(input())))