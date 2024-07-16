#Write a program that uses a class attribute to define some default titles
#for faculty in a college.
#Display the name along with title and department of the college
class CollegeFaculty:
    default_titles = {
        'professor': 'Professor',
        'associate_prof': 'Associate Professor',
        'assistant_prof': 'Assistant Professor'
    }

    def __init__(self, name, title, department):
        self.name = name
        self.title = title
        self.department = department

    def display_info(self):
        if self.title in CollegeFaculty.default_titles:
            full_title = CollegeFaculty.default_titles[self.title]
        else:
            full_title = self.title

        print(f"Name: {self.name}")
        print(f"Title: {full_title}")
        print(f"Department: {self.department}")

# Example usage
faculty_member = CollegeFaculty("nav", "professor", "CSE")
faculty_member.display_info()
