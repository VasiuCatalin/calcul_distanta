notare=float(input("Introduceti o nota de la 0-100: "))
if 0<=notare<=100:
    if notare>=90:
        nota='A'
    elif notare >= 80:
        nota='B'
        nota = 'C'
    elif notare >= 60:
        nota='D'
    else:
        nota='F'
    print("NOTA:", nota)
else:
    print("Notare invalida. Va rog introduceti o nota intre 0-100")
