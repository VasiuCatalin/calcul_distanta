import math


# Funcție pentru a calcula al n-lea număr Fibonacci folosind memoizare
def fibonacci(n, memo=None):
    if n < 0:
        raise ValueError("Fibonacci nu este definit pentru numere negative.")

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


# Funcție pentru calculul ariei unui cerc
def circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise ValueError("Raza trebuie să fie un număr.")
    if radius < 0:
        raise ValueError("Raza nu poate fi negativă.")
    return math.pi * radius ** 2


# Funcție pentru a găsi valoarea maximă dintr-o listă
def find_max(numbers):
    if not numbers:
        raise ValueError("Lista nu poate fi goală.")

    current_max = numbers[0]
    for num in numbers[1:]:
        if num > current_max:
            current_max = num
    return current_max


# Funcție pentru media geometrică a unei liste de numere
def geometric_mean(numbers):
    if not numbers:
        raise ValueError("Lista nu poate fi goală.")
    if any(num <= 0 for num in numbers):
        raise ValueError("Toate numerele trebuie să fie pozitive pentru media geometrică.")

    product = 1
    for num in numbers:
        product *= num
    return product ** (1 / len(numbers))


# Funcția principală
def main():
    print("=== Fibonacci ===")
    try:
        n = int(input("Introduceți un număr pentru calculul Fibonacci: "))
        print(f"Al {n}-lea număr Fibonacci este: {fibonacci(n)}")
    except ValueError as e:
        print(f"Eroare: {e}")

    print("\n=== Aria Cercului ===")
    try:
        radius = float(input("Introduceți raza cercului: "))
        print(f"Aria cercului cu raza {radius} este: {circle_area(radius)}")
    except ValueError as e:
        print(f"Eroare: {e}")

    print("\n=== Maxim din Listă ===")
    try:
        numbers = list(map(float, input("Introduceți numere separate prin spațiu: ").split()))
        print(f"Valoarea maximă din listă este: {find_max(numbers)}")
    except ValueError as e:
        print(f"Eroare: {e}")

    print("\n=== Media Geometrică ===")
    try:
        numbers = list(map(float, input("Introduceți numere pozitive separate prin spațiu: ").split()))
        print(f"Media geometrică este: {geometric_mean(numbers)}")
    except ValueError as e:
        print(f"Eroare: {e}")


# Asigură-te că main() se execută doar când rulăm direct acest fișier
if __name__ == "__main__":
    main()
