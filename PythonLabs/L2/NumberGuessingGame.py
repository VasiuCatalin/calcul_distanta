import random

#setarea limitelor de la tastatura

low=int(input("introduceti limita inferioara: "))
high=int(input("introduceti limita superioara: "))

#generam un numar aleatoriu intre limitele introduse
numar=random.randint(low,high) #alegem un numar aleatoriu specificat de noi

print(f"ghiceste numarul intre {low} si {high}!")

incercari=0
while True:
    incercare=int(input("introdu numarul: "))
    incercari +=1
    if incercare < numar:
        print("prea mic , incearca un numar mai mare.")
    elif incercare > numar:
        print("prea mare, incearca un numar mai mic.")
    else:
        print(f"FELICITARI ai gasit numarul {numar} in {incercari} incercari")
        break