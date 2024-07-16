class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imaginary = imag
    def input_complex(self):
        self.real = float(input("Enter the real part of the complex number: "))
        self.imaginary = float(input("Enter the imaginary part of the complex number: "))
    def display_complex(self):
        print(f"{self.real} + {self.imaginary}i")
# Menu function
def menu():
    print("\nMenu:")
    print("1. Add a complex number")
    print("2. Display all complex numbers")
    print("3. Add all complex numbers")
    print("4. Exit")
    choice = int(input("Enter your choice (1-4): "))
    return choice
# Create an empty list to store complex numbers
complex_numbers = []
while True:
    user_choice = menu()
    if user_choice == 1:
        new_complex = ComplexNumber()
        new_complex.input_complex()
        complex_numbers.append(new_complex)
        print("Complex number added successfully!")
    elif user_choice == 2:
        print("\nDisplaying all complex numbers:")
        for i, complex_num in enumerate(complex_numbers, 1):
            print(f"Complex number {i}: ", end="")
            complex_num.display_complex()
    elif user_choice == 3:
        if len(complex_numbers) < 2:
            print("Add at least two complex numbers to perform addition.")
        else:
            result = ComplexNumber()
            for complex_num in complex_numbers:
                result.real += complex_num.real
                result.imaginary += complex_num.imaginary
            print("\nSum of all complex numbers is:", end=" ")
            result.display_complex()
    elif user_choice == 4:
        print("Exiting the program...")
        break
    else:
        print("Invalid choice! Please enter a valid option (1-4).")
