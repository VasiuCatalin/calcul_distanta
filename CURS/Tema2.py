# Inițializare date
preturi_produse, stoc_initial, vanzari_zi = {}, {}, []
print("Introduceți prețurile (stop pentru a opri):")
while (produs := input("Produs: ")) != 'stop': preturi_produse[produs] = float(input("Preț: "))
print("Introduceți stocurile inițiale (stop pentru a opri):")
while (produs := input("Produs: ")) != 'stop': stoc_initial[produs] = int(input("Stoc: "))
print("Introduceți vânzările (stop pentru a opri):")
while (produs := input("Produs: ")) != 'stop': vanzari_zi.append((produs, int(input("Cantitate: "))))

# Procesarea vânzărilor
venit_total, produse_realimentare = 0, set()
for produs, cantitate in vanzari_zi:
    if produs in preturi_produse and produs in stoc_initial:
        venit_total += preturi_produse[produs] * cantitate
        stoc_initial[produs] -= cantitate
        if stoc_initial[produs] < 5: produse_realimentare.add(produs)

# Raport final
print(f"\nVenit total: {venit_total:.2f} RON\nStocuri rămase:")
for produs, cantitate in stoc_initial.items(): print(f"  - {produs}: {cantitate}")
print("Produse ce necesită realimentare:")
for produs in produse_realimentare: print(f"  - {produs}")
