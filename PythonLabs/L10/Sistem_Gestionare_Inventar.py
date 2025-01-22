class Inventar:
    def __init__(self):
        self.produse = {}  # Stocăm produsele într-un dicționar

    def adauga_produs(self, nume, cantitate):
        """Adaugă un produs nou sau actualizează cantitatea dacă există deja."""
        try:
            cantitate = int(cantitate)  # Convertim la întreg
            if cantitate < 0:
                raise ValueError("Cantitatea nu poate fi negativă!")
            if nume in self.produse:
                self.produse[nume] += cantitate
            else:
                self.produse[nume] = cantitate
            print(f"Produsul '{nume}' a fost adăugat/actualizat cu succes!")
        except ValueError:
            print("Eroare: Introduceți o cantitate validă (număr întreg pozitiv)!")

    def cauta_produs(self, nume):
        """Caută un produs după nume și returnează cantitatea."""
        if nume in self.produse:
            print(f"Produs: {nume}, Cantitate: {self.produse[nume]}")
        else:
            print(f"Eroare: Produsul '{nume}' nu există în inventar!")

    def actualizeaza_cantitate(self, nume, cantitate):
        """Actualizează cantitatea unui produs existent."""
        try:
            cantitate = int(cantitate)
            if cantitate < 0:
                raise ValueError("Cantitatea nu poate fi negativă!")
            if nume in self.produse:
                self.produse[nume] = cantitate
                print(f"Produsul '{nume}' a fost actualizat la {cantitate} bucăți.")
            else:
                print(f"Eroare: Produsul '{nume}' nu există în inventar!")
        except ValueError:
            print("Eroare: Introduceți o cantitate validă (număr întreg pozitiv)!")

    def afiseaza_inventar(self):
        """Afișează toate produsele din inventar."""
        if self.produse:
            print("\nInventar:")
            for nume, cantitate in self.produse.items():
                print(f"- {nume}: {cantitate} bucăți")
        else:
            print("Inventarul este gol!")


# Program principal
inventar = Inventar()

while True:
    print("\nMeniu:")
    print("1. Adaugă produs")
    print("2. Caută produs")
    print("3. Actualizează cantitatea")
    print("4. Afișează inventarul")
    print("5. Ieșire")

    optiune = input("Alege o opțiune: ")

    if optiune == "1":
        nume = input("Introdu numele produsului: ")
        cantitate = input("Introdu cantitatea: ")
        inventar.adauga_produs(nume, cantitate)

    elif optiune == "2":
        nume = input("Introdu numele produsului: ")
        inventar.cauta_produs(nume)

    elif optiune == "3":
        nume = input("Introdu numele produsului: ")
        cantitate = input("Introdu noua cantitate: ")
        inventar.actualizeaza_cantitate(nume, cantitate)

    elif optiune == "4":
        inventar.afiseaza_inventar()

    elif optiune == "5":
        print("Ieșire... La revedere!")
        break

    else:
        print("Opțiune invalidă! Alege un număr între 1 și 5.")
