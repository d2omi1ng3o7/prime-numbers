import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_spiral(size):
    spiral = [[0] * size for _ in range(size)]
    x, y = size // 2, size // 2
    dx, dy = 0, -1
    for i in range(1, size**2 + 1):
        spiral[x][y] = i
        nx, ny = x + dx, y + dy
        if 0 <= nx < size and 0 <= ny < size and spiral[nx][ny] == 0:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy
    return spiral

def count_primes_on_diagonals(spiral):
    n = len(spiral)
    count = 0
    for i in range(n):
        count += is_prime(spiral[i][i])
        count += is_prime(spiral[i][n - i - 1])
    return count

size = 1001
spiral = generate_spiral(size)
primes_count = count_primes_on_diagonals(spiral)

print(f"Na przekątnych spirali o wielkości {size} znajduje się {primes_count} liczb pierwszych.")