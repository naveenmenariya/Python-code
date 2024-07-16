#A program that has a class fraction with attributes numerator and denominator.
#Enter the values of the attributes and print the fraction in simplified form
class fraction:
    '''This is docstring. I have created a new class'''

    def get_data(self):
        self.__num = int(input("Enter the numerator: "))
        self.__deno = int(input("Enter the denominator: "))
        if self.__num == 0:
            print("Fraction not possible")
            exit()

    def display(self):
        self.__simplify()
        print(f"The simplified fraction is: {self.__num}/{self.__deno}")

    def __simplify(self):
        print("The simplified fraction is: ")
        common_divisor = self.__GCD(self.__num, self.__deno)
        self.__num = self.__num // common_divisor
        self.__deno = self.__deno // common_divisor

    def __GCD(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

f = fraction()
f.get_data()
f.display()

