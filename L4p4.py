#Write a program with class Employee that keeps a track of
#the number of employees in an
#organization and also stores their name, designation, and salary details. 
class Employee:
    empCount = 0
    def __init__(self,name,designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print("There are %d employees " %Employee.empCount)
    def displayDetails(self):
        print("Name : ",self.name,", Designation : ",self.designation,", Salary :",self.salary)
e1 = Employee("Farhan", "Manager", 100000)
e2 = Employee("Mike", "Team Leader",90000)
e3 = Employee("Niyam", "Programmer", 80000)
e4 = Employee("Anand", "Office Assistance", 60000)
e4.displayCount()
print("The details of second employee are \n")
e2.displayDetails()
