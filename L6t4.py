class Family:
    def __init__(self, surname):
        self.surname = surname

class Father(Family):
    def __init__(self, surname, name, occupation):
        self.name = name
        self.occupation = occupation

class Mother(Family):
    def __init__(self, surname, name, age):
        super().__init__(surname)
        self.name = name
        self.age = age

class Child(Father, Mother):
    def __init__(self, surname, father_name, father_occ, mother_name, mother_age, child_name):
        # Call the initialization of both Father and Mother separately
        Father.__init__(self, surname, father_name, father_occ)
        Mother.__init__(self, surname, mother_name, mother_age)
        self.child_name = child_name

    def print_details(self):
        print("Family Surname:", self.surname)
        print("Father:", self.name, self.occupation)
        print("Mother:", self.name, self.age)
        print("Child Name:", self.child_name)

child1 = Child("Smith", "John", "Engineer", "Mary", 45, "Mark")
child1.print_details()
