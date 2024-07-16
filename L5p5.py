#A menu driven program that keeps record of books and
#journals available in a library
class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.price = 0
    def read(self):
        self.title = input("Enter Book title:")
        self.author = input("Enter Book author:")
        self.price = input("Enter Book price:")
    def display(self):
        print("TItle : ", self.title)
        print("Author : ", self.author)
        print("Price : ", self.price)
my_books = []
ch = 'y'
while (ch == 'y'):
    print('''1. Add New Book 2. Display book ''')
    choice = int(input("Enter choice: "))
    if (choice == 1):
        book = Book()
        book.read()
        my_books.append(book)
    elif(choice==2):
        for i in my_books:
            i.display()
    else:
        print("Invalid choice")
    ch = input("Do you want to continue..")
print("Bye")
