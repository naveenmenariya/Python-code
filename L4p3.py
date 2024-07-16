class Circle:
    PI = 3.1415
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return Circle.PI*self.radius*self.radius
    def crecumference(self) :
        return Circle.PI*2*self.radius

C = Circle(7.5)
print("Area is :", C.area())
print("crecumference is :", C.crecumference())
