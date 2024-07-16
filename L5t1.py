class fraction:
    ''' This is docstring. I have created a new class '''

    def __init__(self, num=0, deno=1):
        if deno == 0:
            print("Denominator cannot be zero. Fraction not possible.")
            exit()
        self.__num = num
        self.__deno = deno
    def display(self):
        self.__simplify()
        print(f"{self.__num}/{self.__deno}")
    def __simplify(self):
        print("The simplified fraction is: ")
        common_divisor = self.__GCD(self.__num, self.__deno)
        self.__num = self.__num // common_divisor
        self.__deno = self.__deno // common_divisor
    def __GCD(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    def add(self, other_fraction):
        new_num = self.__num * other_fraction.__deno + other_fraction.__num * self.__deno
        new_deno = self.__deno * other_fraction.__deno
        return fraction(new_num, new_deno)
    def subtract(self, other_fraction):
        new_num = self.__num * other_fraction.__deno - other_fraction.__num * self.__deno
        new_deno = self.__deno * other_fraction.__deno
        return fraction(new_num, new_deno)
# Example usage
f1 = fraction(1, 2)  # Enter your fraction's numerator and denominator here
f1.display()
f2 = fraction(1, 3)  # Enter your fraction's numerator and denominator here
f2.display()
result_add = f1.add(f2)
print("Addition:", end=" ")
result_add.display()
result_subtract = f1.subtract(f2)
print("Subtraction:", end=" ")
result_subtract.display()
