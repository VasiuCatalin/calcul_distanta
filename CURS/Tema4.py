import os

CALE_FISIER="filme.txt"

#functie pentru incarcarea filmelor din fisier
def incarca_filme():
    filme={}
    if os.path.exists(CALE_FISIER):
        with open(CALE_FISIER,"r") as fisier:
            for linie in fisier:1

            titlu, evaluare =linie.strip().split(", ")
            filme[titlu]=int(evaluare)
        return filme

#functie pentru salvarea filmelor in fisier
def salveaza_filme(filme):
    with open(CALE_FISIER,"w") as fisier:
        for titlu, evaloare in sorted(filme.items(), key=lambda x: (-x[1], x[0])):
           fisier.write(f"{titlu}, {evaloare}\n")

#functie pentru afisarea tuturor filmelor si a evaluarilor acestora
def afiseaza_filme(filme):
    if not filme:
        print("\nNu exista filme in lista.")
    else:
        for titlu, evaluare in sorted(filme.items(), key=lambda x: (-x[1], x[0])):
            print(f"{titlu}: {evaluare}")

#functie pentru adaugarea sau actualizarea evaluarii unui film
def adauga_sau_actualizeaza_film(filme):
    titlu=input("\nIntroduceti titlul filmului: ").strip()
    while True:
        try:
            evaluare=int(input("Introduceti evaluarea (1-5): ").strip())
            if 1<= evaluare <=5:
                break
            else:
                print("Evaluarea trebuie sa fie intre 1 si 5.")
        except ValueError:
            print("Va rugam sa introduceti un numar valid.")
    filme[titlu]=evaluare
    print(f"Filmul {titlu} a fost adaugat/actualizat cu evaluarea {evaluare}.")

#functia pentru stergerea unui film
def sterge_film(filme):
    titlu=input("\nIntroduceti titlul filmului de sters: ").strip()
    if titlu in filme:
        del filme[titlu]
        print(f"Filmul {titlu} a fost sters.")
    else:
        print(f"Filmul {titlu} nu exista in lista.")

#bucle principale ale programului
def main():
    filme=incarca_filme()
    while True:
        print("\nSelectati o optiune:")
        print("1. Vizualizare filme si evaluari")
        print("2. Adaugare/Actualizare evaluare film")
        print("3. Stergere film")
        print("4. Salvare si iesire")
        optiune=input("\nOptiunea dumneavoastra: ").strip()

        if optiune=="1":
            afiseaza_filme(filme)
        elif optiune=="2":
            adauga_sau_actualizeaza_film(filme)
        elif optiune=="3":
            sterge_film(filme)
        elif optiune=="4":
            salveaza_filme(filme)
            print("Modificarile au fost salvate.")
            break
        else:
            print("Optiune invalida, incearca din nou. ")

if __name__=="__main__":
    main()