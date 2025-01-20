class Carte:
    def __init__(self, titlu, autor, isbn):
        self.titlu = titlu
        self.autor = autor
        self.isbn = isbn
        self.este_imprumutata = False

    def __str__(self):
        return f"{self.titlu} de {self.autor} (ISBN: {self.isbn}) - {'Împrumutată' if self.este_imprumutata else 'Disponibilă'}"


class MembruBiblioteca:
    def __init__(self, nume):
        self.nume = nume
        self.carti_imprumutate = []

    def imprumuta_carte(self, carte):
        if not carte.este_imprumutata:
            carte.este_imprumutata = True
            self.carti_imprumutate.append(carte)
            print(f"{self.nume} a împrumutat cartea: {carte.titlu}")
        else:
            print(f"Cartea {carte.titlu} este deja împrumutată!")

    def returneaza_carte(self, carte):
        if carte in self.carti_imprumutate:
            carte.este_imprumutata = False
            self.carti_imprumutate.remove(carte)
            print(f"{self.nume} a returnat cartea: {carte.titlu}")
        else:
            print(f"{self.nume} nu are această carte împrumutată!")


class Biblioteca:
    def __init__(self):
        self.carti = []

    def adauga_carte(self, carte):
        self.carti.append(carte)
        print(f"Cartea {carte.titlu} a fost adăugată în bibliotecă.")

    def sterge_carte(self, carte):
        if carte in self.carti:
            self.carti.remove(carte)
            print(f"Cartea {carte.titlu} a fost ștearsă din bibliotecă.")
        else:
            print(f"Cartea {carte.titlu} nu se află în bibliotecă!")

    def listeaza_carti_disponibile(self):
        print("Cărți disponibile:")
        for carte in self.carti:
            if not carte.este_imprumutata:
                print(f"- {carte}")


# Creare bibliotecă
biblioteca = Biblioteca()

# Adăugare cărți de la tastatură
numar_carti = int(input("Introdu numărul de cărți: "))
for _ in range(numar_carti):
    titlu = input("Titlul cărții: ")
    autor = input("Autorul cărții: ")
    isbn = input("ISBN-ul cărții: ")
    biblioteca.adauga_carte(Carte(titlu, autor, isbn))

# Creare membri
membri = []
numar_membri = int(input("Introdu numărul de membri ai bibliotecii: "))
for _ in range(numar_membri):
    nume = input("Numele membrului: ")
    membri.append(MembruBiblioteca(nume))

# Simulare împrumut și returnare
while True:
    print("\n1. Listează cărți disponibile")
    print("2. Împrumută o carte")
    print("3. Returnează o carte")
    print("4. Ieșire")
    optiune = input("Alege o opțiune: ")

    if optiune == "1":
        biblioteca.listeaza_carti_disponibile()
    elif optiune == "2":
        nume_membru = input("Introdu numele membrului: ")
        titlu_carte = input("Introdu titlul cărții: ")
        membru = next((m for m in membri if m.nume == nume_membru), None)
        carte = next((c for c in biblioteca.carti if c.titlu == titlu_carte), None)
        if membru and carte:
            membru.imprumuta_carte(carte)
        else:
            print("Membru sau carte inexistentă!")
    elif optiune == "3":
        nume_membru = input("Introdu numele membrului: ")
        titlu_carte = input("Introdu titlul cărții: ")
        membru = next((m for m in membri if m.nume == nume_membru), None)
        carte = next((c for c in biblioteca.carti if c.titlu == titlu_carte), None)
        if membru and carte:
            membru.returneaza_carte(carte)
        else:
            print("Membru sau carte inexistentă!")
    elif optiune == "4":
        break
    else:
        print("Opțiune invalidă!")
