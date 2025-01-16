def inverseaza_cuvintele(propozitie):
    cuvinte=propozitie.strip()
    print(f"Propozitia dupa strip: '{propozitie}'")
    cuvinte=propozitie.split()
    print(f"Cuvinte separate: {cuvinte}")
    if not cuvinte:
        return "Nu ai introdus niciun cuvant."
    cuvinte_inverse=cuvinte[::-1]
    print(f"Cuvinte inversate:{cuvinte_inverse}")
    propozitie_inversata= ' '.join(cuvinte_inverse)
    print(f"Propozitie inversata: '{propozitie_inversata}'")
    return propozitie_inversata
propozitie=input("Introduceti o propozitie: ")
rezultat=inverseaza_cuvintele(propozitie)
print("Propozitia cu cuvintele inversate este:", rezultat)