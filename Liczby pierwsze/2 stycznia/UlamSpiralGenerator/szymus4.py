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

    return ulam, (max_x, max_y)

def print_ulam_spiral(ulam):
    size = len(ulam)
    for i in range(size):
        for j in range(size):
            if ulam[i][j] == 0:
                print('\033[0m', end='\t')
            elif is_prime(ulam[i][j]):
                print('\033[91m', ulam[i][j], '\033[0m', end='\t')
            else:
                if ulam[i][j] < 10:
                    print(' ', ulam[i][j], end='\t')
                else:
                    print(ulam[i][j], end='\t')
        print()

size = 15
ulam, (max_x, max_y) = generate_ulam_spiral(size)
print_ulam_spiral(ulam)

print(f"Największa widoczna na spirali liczba pierwsza to i znajduje się na koordynatach ({max_x}, {max_y})") 