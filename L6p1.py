class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

class Teacher(Person):
    def __init__(self,name,age,exp,r_area):
        Person.__init__(self,name,age)
        self.exp = exp
        self.r_area = r_area
    def displayData(self):
        Person.display(self)
        print("Experience: ",self.exp)
        print("Research Area: ",self.r_area)
class Student(Person):
    def __init__(self,name,age,course,marks):
        Person.__init__(self,name,age)
        self.course = course
        self.marks = marks
    def displayData(self):
        Person.display(self)
        print("Course: ",self.course)
        print("Marks obtained: ",self.marks)
print("*********TEACHER********")
T = Teacher("OVR",45,10,"Machine Learning")
T.displayData()
print('*********STUDENT********')
S = Student("Anoop",20,"BTech",85)
S.displayData()
print("T is a Teacher: ",isinstance(T,Teacher))#Person, int
print("Person is a subclass of Teacher: ", issubclass(Person,Teacher))#Person, int
