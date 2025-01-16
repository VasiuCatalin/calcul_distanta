def unique_pair_sum(nums, target):
    pairs=set() #folosesc un set pentru a asigura unicitatea perechilor
    #creeaz un set pentru a verifica daca complementul exista
    seen=set()
    for num in nums:
        complement=target-num
        if complement in seen:
            #adaugam perechea ordomanata (a,b), unde a<=b
            pair=tuple(sorted((num, complement)))
            pairs.add(pair)
        seen.add(num)
    return pairs

#citim lista de numere si numarul pe care vrem sa il afisam
nums=list(map(int, input("Introdu lista de numere separate prin spatiu: ").split()))
target=int(input("Introdu valoarea tinta: "))
#afisam perechile care adunate dau valoarea tinta
result= unique_pair_sum(nums, target)
print(f"Perecgile unice care adunate dau {target} sunt: {result}")

