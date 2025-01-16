# Introducere date
print("Introduceți produse și prețuri (stop pentru a opri):")
produse_preturi = [(produs, float(input(f"Preț pentru {produs}: "))) for produs in iter(lambda: input("Produs: "), 'stop')]
print("Introduceți stocurile inițiale (stop pentru a opri):")
stoc_initial = [(produs, int(input(f"Stoc pentru {produs}: "))) for produs in iter(lambda: input("Produs: "), 'stop')]
print("Introduceți vânzările (stop pentru a opri):")
vanzari_zi = [(produs, int(input(f"Cantitate pentru {produs}: "))) for produs in iter(lambda: input("Produs: "), 'stop')]

# Procesare
venit_total = 0
stoc_actualizat = {prod: cant for prod, cant in stoc_initial}
preturi = {prod: pret for prod, pret in produse_preturi}

for produs, cantitate in vanzari_zi:
    if produs in stoc_actualizat and produs in preturi:
        venit_total += preturi[produs] * cantitate
        stoc_actualizat[produs] -= cantitate

# Realimentare
produse_realimentare = {prod for prod, cant in stoc_actualizat.items() if cant < 5}

# Raport
print(f"\nVenit total: {venit_total:.2f} RON\nStocuri rămase:")
[print(f"  - {prod}: {cant}") for prod, cant in stoc_actualizat.items()]
print("Produse ce necesită realimentare:")
[print(f"  - {prod}") for prod in produse_realimentare]
