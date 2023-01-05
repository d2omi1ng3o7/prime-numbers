from math import sqrt


lpn = 7
f1 = lambda x: x*3 + 2
f2 = lambda x: x*3 + 4
i = 1

def ifPrimeNumber(num):
    for x in range(7, num//2+1, 2):
        if num % x == 0:
            return False
    return True

try:
    while True:
        for f in (f1, f2):
            num = f(i)
            if ifPrimeNumber(num):
                lpn = num             
        i += 2
except:
    print(f'{lpn}')