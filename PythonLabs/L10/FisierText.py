import os

def creeaza_fisier_daca_nu_exista(nume_fisier):
    """ Creează un fișier cu numere dacă nu există deja. """
    if not os.path.exists(nume_fisier):
        print(f"Fișierul '{nume_fisier}' nu există. Se creează unul nou...")
        with open(nume_fisier, "w") as fisier:
            fisier.write("10\n20.5\n30\n40\n50.7\n")  # Scrie câteva numere exemplu
        print(f"Fișierul '{nume_fisier}' a fost creat cu succes!")

def calculeaza_suma_din_fisier(nume_fisier):
    """ Citește un fișier și calculează suma numerelor, gestionând erorile. """
    try:
        suma = 0
        with open(nume_fisier, "r") as fisier:
            for linie in fisier:
                try:
                    suma += float(linie.strip())  # Convertim linia în număr
                except ValueError:
                    print(f"Eroare: '{linie.strip()}' nu este un număr valid și va fi ignorat.")
        print(f"Suma numerelor din fișier este: {suma}")
    except IOError:
        print("Eroare: Nu s-a putut citi fișierul!")

# Program principal
nume_fisier = "numere.txt"
creeaza_fisier_daca_nu_exista(nume_fisier)
calculeaza_suma_din_fisier(nume_fisier)
