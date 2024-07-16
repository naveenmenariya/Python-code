#Program to demonstrate the use of built-in functions
class ABC:
    def __init__(self, var):
        self.var = var

    def display(self):
        if hasattr(self, 'var'):
            print("Var is =", self.var)
        else:
            print("Var attribute doesn't exist")

obj = ABC(10)
obj.display()
print("Check attribute var ...", hasattr(obj, 'var'))  # TRUE
print("Check attribute count ...", hasattr(obj, 'count'))  # FALSE
setattr(obj, 'var', 50)
obj.display()
print(getattr(obj, 'count', 'Attribute not found'))
setattr(obj, 'count', 20)
print(obj.count)
delattr(obj, 'var')
obj.display()
