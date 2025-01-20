# math_operations.py

def adunare():
    a = float(input("Introduceți primul număr pentru adunare: "))
    b = float(input("Introduceți al doilea număr pentru adunare: "))
    return a + b

def scadere():
    a = float(input("Introduceți primul număr pentru scădere: "))
    b = float(input("Introduceți al doilea număr pentru scădere: "))
    return a - b

def inmultire():
    a = float(input("Introduceți primul număr pentru înmulțire: "))
    b = float(input("Introduceți al doilea număr pentru înmulțire: "))
    return a * b

def impartire():
    a = float(input("Introduceți primul număr pentru împărțire: "))
    b = float(input("Introduceți al doilea număr pentru împărțire: "))
    if b != 0:
        return a / b
    else:
        return "Eroare: Împărțirea la zero nu este permisă!"

