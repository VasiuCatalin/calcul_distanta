def imparte_numere():
    try:
        num1 = float(input("Introduceți primul număr: "))
        num2 = float(input("Introduceți al doilea număr: "))
        rezultat = num1 / num2
        print(f"Rezultatul împărțirii este: {rezultat}")
    except ZeroDivisionError:
        print("Eroare: Împărțirea la zero nu este permisă!")
    except ValueError:
        print("Eroare: Introduceți doar numere valide!")

# Apelul funcției
imparte_numere()
