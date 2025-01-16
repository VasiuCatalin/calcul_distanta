#introducerea propozitiei de la utilizator
propozitie=input("introduceti o propozitie: ")

#introducerea cuvantului de la utilizator
cuvant=input("Introduceti cuvantul pe care doresti sa il numeri: ")

#numara aparitiile cuvantului in propozitie
numar_aparitii=propozitie.split().count(cuvant)

#afisarea numarului de aparitii
print(f"Cuvantul {cuvant} apare de {numar_aparitii} ori in propozitia data. ")
