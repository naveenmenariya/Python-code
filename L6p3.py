class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f'Name: {self.name}')


class Teacher(Person):
    def __init__(self, name, qualification):
        super().__init__(name)
        self.qualification = qualification

    def display_qualification(self):
        print(f'Qualification: {self.qualification}. PhD mandatory')


class HOD(Teacher):
    def __init__(self, name, qualification, experience):
        super().__init__(name, qualification)
        self.experience = experience

    def display_experience(self):
        print(f'Experience: {self.experience}. At least 15 years')


# Creating an instance of HOD
hod = HOD("John Doe", "Mathematics", 20)
hod.display_name()  # Use display_name method to print the name
hod.display_qualification()
hod.display_experience()
