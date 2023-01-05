from math import sqrt

how = int(input('Ilość iteracji: '))
f1 = lambda x: x*3 + 2
f2 = lambda x: x*3 + 4
primeNumbers = []
for x in range(1, how, 2):
    for f in (f1, f2):
        num = f(x)
        if num % sqrt(num) == 0 or num % 5 == 0 or num % 7 == 0:
            pass
        else:
            primeNumbers.append(num)
            
print('success')
print(len(primeNumbers)+4)
print(f'do liczby {primeNumbers[-1]}')