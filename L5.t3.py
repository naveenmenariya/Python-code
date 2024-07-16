class NumberList:
    def __init__(self):
        self.numbers = []

    def read(self):
        num_str = input("Enter numbers separated by spaces: ")
        self.numbers = list(map(int, num_str.split()))

    def display(self):
        print("Numbers in the list:", self.numbers)

    def find_largest(self):
        if not self.numbers:
            print("List is empty")
            return None
        return max(self.numbers)

    def sum(self):
        return sum(self.numbers)

    def find_mean(self):
        if not self.numbers:
            print("List is empty")
            return None
        return sum(self.numbers) / len(self.numbers)


# Example usage
num_list = NumberList()
num_list.read()
num_list.display()

largest = num_list.find_largest()
if largest is not None:
    print("Largest number in the list:", largest)

sum_of_numbers = num_list.sum()
print("Sum of numbers:", sum_of_numbers)

mean = num_list.find_mean()
if mean is not None:
    print("Mean of the numbers:", mean)
