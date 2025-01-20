# Structura directorului:
# geometry/
# ├── __init__.py
# ├── circle.py
# ├── rectangle.py
# ├── main.py

# geometry/circle.py
import math

def aria_cerc(raza):
    return math.pi * raza ** 2

def circumferinta_cerc(raza):
    return 2 * math.pi * raza

# geometry/rectangle.py
def aria_dreptunghi(latime, inaltime):
    return latime * inaltime

def perimetru_dreptunghi(latime, inaltime):
    return 2 * (latime + inaltime)

# geometry/__init__.py
from .circle import aria_cerc, circumferinta_cerc
from .rectangle import aria_dreptunghi, perimetru_dreptunghi

# main.py
import geometry

raza = float(input("Introduceți raza cercului: "))
print(f"Aria cercului: {geometry.aria_cerc(raza)}")
print(f"Circumferința cercului: {geometry.circumferinta_cerc(raza)}")

latime = float(input("Introduceți lățimea dreptunghiului: "))
inaltime = float(input("Introduceți înălțimea dreptunghiului: "))
print(f"Aria dreptunghiului: {geometry.aria_dreptunghi(latime, inaltime)}")
print(f"Perimetrul dreptunghiului: {geometry.perimetru_dreptunghi(latime, inaltime)}")
