import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_ulam_spiral(size):
    ulam = [[0] * size for i in range(size)]
    x, y = size // 2, size // 2
    ulam[x][y] = 1

    dx, dy = 0, -1
    for i in range(2, size**2 + 1):
        if (x + dx < 0 or x + dx >= size or y + dy < 0 or y + dy >= size or ulam[x+dx][y+dy] != 0):
            dx, dy = dy, -dx
        x, y = x + dx, y + dy
        ulam[x][y] = i if is_prime(i) else 0

    return ulam

size = 15
ulam = generate_ulam_spiral(size)
for i in range(size):
    for j in range(size):
        print(ulam[i][j], end='\t')
    print()