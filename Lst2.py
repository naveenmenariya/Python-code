class ABC():
    def __init__(self,var1,var2):
        self.var1 = var1
        self.var2 = var2
    def display(self):
        print("Var 1 is ",self.var1)
        print("Var 2 is ",self.var2)
obj = ABC(10,3.14)
obj.display()
print("Object.__doc__ is",obj.__doc__)
print("Class.__name__ is",ABC.__name__)
print("Object.__module__ is",obj.__module__)
