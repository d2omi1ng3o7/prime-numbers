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
    max_prime = 0
    max_x, max_y = x, y
    for i in range(2, size**2 + 1):
        if (x + dx < 0 or x + dx >= size or y + dy < 0 or y + dy >= size or ulam[x+dx][y+dy] != 0):
            dx, dy = dy, -dx
        x, y = x + dx, y + dy
        if is_prime(i):
            ulam[x][y] = i
            if i > max_prime:
                max_prime = i
                max_x, max_y = x, y

    return ulam, (max_x, max_y), max_prime

size = 15
ulam, (max_x, max_y), max_prime = generate_ulam_spiral(size)
for i in range(size):
    for j in range(size):
        print(ulam[i][j], end='\t')
    print()

print(f"Największa widoczna na spirali liczba pierwsza to {max_prime} i znajduje się na koordynatach ({max_x}, {max_y})")