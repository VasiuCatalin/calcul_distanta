import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle with radius {self.radius} has area {self.area():.2f}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle with width {self.width} and height {self.height} has area {self.area()}"

# Introducerea datelor de la tastatură
radius = float(input("Enter the radius of the circle: "))
width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))

# Crearea obiectelor folosind datele introduse
circle = Circle(radius)
rectangle = Rectangle(width, height)

# Afisarea detaliilor folosind __str__
print(circle)     # "Circle with radius X has area Y"
print(rectangle)  # "Rectangle with width X and height Y has area Z"
