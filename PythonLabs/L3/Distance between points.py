import math

def distanta(punct1, punct2):
    return math.sqrt((punct2[0]-punct1[0])**2 +(punct2[1]-punct1[1])**2)

x1=float(input("Introduceti coordonata x a primului punct: "))
y1=float(input("Introduceti coordonata y a primului punct: "))

x2=float(input("Introduceti coordonata x pt al doilea punct: "))
y2=float(input("Introduceti coordonata y pt al doilea punct: "))

punct1=(x1 ,y1)
punct2=(x2, y2)
print(f"Distanta dintre punctele {punct1} si {punct2} este {distanta(punct1, punct2)}")
