from abc import ABC, abstractmethod
class Polygon(ABC):
    def __init__(self, *args):
        self.sides = args
    @abstractmethod
    def get_details(self):
        pass
    @abstractmethod
    def calculate_area(self):
        pass
class Rectangle(Polygon):
    def get_details(self):
        return f"Rectangle sides: {self.sides}"
    def calculate_area(self):
        return self.sides[0] * self.sides[1]

class Square(Polygon):
    def get_details(self):
        return f"Square side: {self.sides[0]}"
    def calculate_area(self):
        return self.sides[0] ** 2

class Triangle(Polygon):
    def get_details(self):
        return f"Triangle sides: {self.sides}"

    def calculate_area(self):
        # Using Heron's formula to calculate the area of a triangle
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area

# Creating instances and calculating areas
rectangle = Rectangle(4, 6)
square = Square(5)
triangle = Triangle(3, 4, 5)
# Displaying details and areas
print(rectangle.get_details())
print(f"Rectangle area: {rectangle.calculate_area()}")

print(square.get_details())
print(f"Square area: {square.calculate_area()}")

print(triangle.get_details())
print(f"Triangle area: {triangle.calculate_area()}")
