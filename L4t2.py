#Create a class that collects two strings as input.
#Class should also contain a method that compares the lengths of
#two strings and displays which string is longest one.
#You can use string library functions. __len()__
class StringComparator:
    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2

    def compare_lengths(self):
        len1 = len(self.string1)
        len2 = len(self.string2)

        if len1 > len2:
            print(f"'{self.string1}' is longer than '{self.string2}'")
        elif len1 < len2:
            print(f"'{self.string2}' is longer than '{self.string1}'")
        else:
            print("Both strings are of equal length")

# Example usage
string_comp = StringComparator("Hello", "naveen")
string_comp.compare_lengths()
