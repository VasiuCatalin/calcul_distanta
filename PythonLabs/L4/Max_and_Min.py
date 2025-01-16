input_numere  = input("Introdu numere separate prin spatiu: ")

# convertim sirul de text intr-o lista de numere
numere= list(map(int, input_numere.split()))
#gasim cel mai mare si cel mai mic numar
maxim=max(numere)
minim=min(numere)

#afisam rezultatele
print("Cel mai mare numar este:", maxim)
print("Cel mai mic numar este", minim)