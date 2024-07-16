import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return (self.x, self.y)


class Location:
    def __init__(self, x1, y1, x2, y2):
        self.source = Point(x1, y1)
        self.destination = Point(x2, y2)

    def show(self):
        print("Source =", self.source.get())
        print("Destination =", self.destination.get())

    def distance(self):
        distance = math.sqrt((self.destination.x - self.source.x) ** 2 + (self.destination.y - self.source.y) ** 2)
        print(f"Distance between Source and Destination: {distance:.2f}")


L = Location(1, 2, 3, 4)
L.show()
L.distance()
