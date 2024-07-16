#Write a program that has a class student with data members – roll number,
#name and marks in three subjects. All the five members are private. 
class student():
    __marks = []
    def set_data(self,roll,name,m1,m2,m3):
        self.__roll = roll
        self.__name = name
        self.__marks.append(m1)
        self.__marks.append(m2)
        self.__marks.append(m3)
    def display(self):
        print("Total marks of ",self.__name," is ", self.total())
    def total(self):
        m = self.__marks
        return m[0]+m[1]+m[2]
s1 = student()
s1.set_data(1,'ovr',10,20,30)
s1.display()
