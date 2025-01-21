import math


# Funcție pentru calcularea celui de-al n-lea număr Fibonacci folosind memoizare
def fibonacci(n, memo=None):
    if n < 0:
        raise ValueError("Fibonacci nu este definit pentru numere negative.")

    # Folosirea valorii None pentru a preveni comportamentele neașteptate cu obiectele mutabile
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        return memo[n]


# Funcție pentru calcularea ariei unui cerc cu validare a intrării
def aria_cercului(raza):
    # Verificarea dacă raza este un număr valid
    if not isinstance(raza, (int, float)):
        raise ValueError("Raza trebuie să fie un număr.")
    if raza < 0:
        raise ValueError("Raza nu poate fi negativă.")
    return math.pi * raza ** 2


# Funcție pentru găsirea valorii maxime dintr-o listă folosind recursivitatea
def gaseste_maxim(numere):
    if not numere:  # Verificare pentru listă goală
        raise ValueError("Nu se poate găsi maximul într-o listă goală.")
    # Soluție iterativă pentru a evita depășirea stivei în cazul listelor mari
    maxim_curent = numere[0]
    for num in numere[1:]:
        if num > maxim_curent:
            maxim_curent = num
    return maxim_curent


# Funcție pentru calcularea mediei geometrice a unei liste de numere
def media_geometrica(numere):
    if not numere:  # Verificare pentru listă goală
        raise ValueError("Nu se poate calcula media geometrică a unei liste goale.")
    # Verificarea ca toate numerele să fie pozitive
    if any(num <= 0 for num in numere):
        raise ValueError("Toate numerele trebuie să fie pozitive pentru media geometrică.")

    produs = 1
    for num in numere:
        produs *= num
    return produs ** (1 / len(numere))


# Funcție principală pentru a demonstra operațiile cu date introduse de utilizator
def principal():
    # Introducerea unui număr pentru Fibonacci
    try:
        n = int(input("Introduceți un număr pentru calculul Fibonacci: "))
        print(f"Al {n}-lea număr Fibonacci este: {fibonacci(n)}")
    except ValueError as e:
        print(e)

    # Introducerea razei cercului
    try:
        raza = float(input("Introduceți raza cercului: "))
        print(f"Aria cercului cu raza {raza} este: {aria_cercului(raza)}")
    except ValueError as e:
        print(e)

    # Introducerea unei liste de numere pentru găsirea maximului
    try:
        numere = list(map(int, input("Introduceți o listă de numere separate prin spațiu: ").split()))
        print(f"Valoarea maximă din listă este: {gaseste_maxim(numere)}")
    except ValueError as e:
        print(e)

    # Introducerea unei liste de numere pentru media geometrică
    try:
        numere = list(map(float, input("Introduceți o listă de numere pozitive pentru media geometrică: ").split()))
        print(f"Media geometrică este: {media_geometrica(numere)}")
    except ValueError as e:
        print(e)


principal()
