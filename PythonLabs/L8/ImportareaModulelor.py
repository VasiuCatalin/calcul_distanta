import math

# Citirea valorilor de la tastatură
num = int(input("Introduceți un număr întreg: "))
angle = float(input("Introduceți un unghi în grade: "))

# Calcularea rădăcinii pătrate
sqrt_num = math.sqrt(num)
print(f"Rădăcina pătrată a {num} este {sqrt_num}")

# Calcularea factorialului
factorial_num = math.factorial(num)
print(f"Factorialul lui {num} este {factorial_num}")

# Calcularea sinusului unghiului în grade
sin_angle = math.sin(math.radians(angle))
print(f"Sinusul unghiului de {angle} grade este {sin_angle}")
