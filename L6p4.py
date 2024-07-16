class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print('Name:', self.name)


class Teacher(Person):
    def __init__(self, name, qualification):
        super().__init__(name)
        self.qualification = qualification

    def display_qualification(self):
        print('Qualification:', self.qualification)


class HOD(Teacher):
    def __init__(self, name, qualification, experience):
        super().__init__(name, qualification)
        self.experience = experience

    def display_experience(self):
        print('Experience:', self.experience, 'years')


# Create an instance of HOD
hod = HOD("", "PhD", 15)

# Call methods to display information
hod.display_name()
hod.display_qualification()
hod.display_experience()
