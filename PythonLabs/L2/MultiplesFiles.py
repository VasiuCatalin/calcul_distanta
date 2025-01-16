#introducerea datelor de la tastatura
limita=int(input("Introduceti limita superioara: "))
div1=int(input("Intoduceti primul divizor: "))
div2=int(input("Introduceti al doilea divizor: "))

#gasirea numerelor

multiplu=[]
for num in range(1,limita):
    if num % div1 == 0 or num % div2 == 0:
        multiplu.append(num) #adauga in lista goala multiplu valoarea num


#afisarea rezultatului
print("Multiplii sunt: ", multiplu)