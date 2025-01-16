numar=int(input("Introduceti un numar: "))
este_prim=True
if numar<2:
    este_prim=False
else:
    for i in range(2, numar):
        if numar %i==0:
            este_prim=False
            break
if este_prim:
    print(f"{numar} este prim.")
else:
    print(f"{numar} nu este prim.")