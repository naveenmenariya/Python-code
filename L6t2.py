class Student:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name


class Grade:
    def __init__(self, CGPA):
        self.CGPA = CGPA


class Scholarship(Student, Grade):
    def __init__(self, ID, name, CGPA):
        Student.__init__(self, ID, name)
        Grade.__init__(self, CGPA)

    def compute_scholarship(self):
        if self.CGPA > 9:
            return "Rs. 10,000/- per month"
        elif self.CGPA > 8:
            return "Rs. 7500/- per month"
        elif self.CGPA > 7.5:
            return "Rs. 5000/- per month"
        else:
            return "No scholarship eligibility"

# Creating an object of Scholarship
student = Scholarship("CSE22127", "Naveen", 9.5)

# Displaying scholarship details
print(f"Student ID: {student.ID}")
print(f"Student Name: {student.name}")
print(f"Scholarship Amount: {student.compute_scholarship()}")
