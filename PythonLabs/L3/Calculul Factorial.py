def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)

numar=int(input("introduceti un numar pentru a calcula factorialul acestuia: "))

print(f"Factorialul lui {numar} este {factorial(numar)}")