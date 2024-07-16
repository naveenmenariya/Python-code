class StudentMarks:
    def __init__(self, name):
        self.name = name
        self.marks = []
    def read_marks(self):
        marks_str = input(f"Enter marks for {self.name} separated by spaces: ")
        self.marks = list(map(int, marks_str.split()))
    def display_marks(self):
        print(f"{self.name}'s marks:", self.marks)
    def calculate_total(self):
        return sum(self.marks)
# Create student objects
student1 = StudentMarks("naveen")
student2 = StudentMarks("raj")
student3 = StudentMarks("nav")
student4 = StudentMarks("kavi")
# Read marks for each student
student1.read_marks()
student2.read_marks()
student3.read_marks()
student4.read_marks()
# Display marks for each student
student1.display_marks()
student2.display_marks()
student3.display_marks()
student4.display_marks()
# Calculate total marks for each student
total_student1 = student1.calculate_total()
total_student2 = student2.calculate_total()
total_student3 = student3.calculate_total()
total_student4 = student4.calculate_total()
# Store student objects and their total marks in a list
students = [
    (student1, total_student1),
    (student2, total_student2),
    (student3, total_student3),
    (student4, total_student4)
]
# Sort students based on total marks in descending order
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
# Display students' records sorted by total marks
print("\nStudents' records sorted by total marks (descending order):")
for student, total_marks in sorted_students:
    print(f"{student.name}: Total Marks - {total_marks}")
