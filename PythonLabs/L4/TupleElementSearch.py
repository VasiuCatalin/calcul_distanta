elements=input("Introdu elementele tuple-ului, separate prin spatiu:").split()
#convertim lista de strng-uri intr-un tuple
my_tuple=tuple(elements)
#introducerea elementului de cautat
element_to_search=input("Introdu elementul pe care vrei sa-l cauti: ")

#vreificam daca elementul exista in tuple
if element_to_search in my_tuple:
    print(f"Elementul {element_to_search} se afla in tuple!")
else:
    print(f"Elementul {element_to_search} nu se afla in tuple.")