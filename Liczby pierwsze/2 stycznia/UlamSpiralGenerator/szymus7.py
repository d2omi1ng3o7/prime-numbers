def sito(n):
    # Tworzymy listę od 2 do n (włącznie)
    numbers = list(range(2, n+1))
 
    # Iterujemy po liczbach
    for i in numbers:
        # Iterujemy po wielokrotnościach i
        for j in range(2*i, n+1, i):
            # Jeśli wielokrotność jest w numbers, usuwamy ją
            if j in numbers:
                numbers.remove(j)
 
    # Zwracamy pozostałe liczby jako wynik
    return numbers

# Przykładowe wywołanie funkcji
sito(10000000) # powinno zwrócić [2, 3, 5, 7, 11, 13, 17, 19]