class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def display(self):
        print(f"Title: {self.title}")
        print(f"Price: Rs.{self.price}")


class Book(Publication):
    def __init__(self, title, price, num_pages):
        super().__init__(title, price)
        self.num_pages = num_pages

    def display(self):
        super().display()
        print(f"Number of Pages: {self.num_pages}")


class CD(Publication):
    def __init__(self, title, price, play_time):
        super().__init__(title, price)
        self.play_time = play_time

    def display(self):
        super().display()
        print(f"Play Time: {self.play_time} minutes")


# Creating objects
book = Book("DSA", 1000, 350)
cd = CD("Music", 800, 60)

# Displaying outputs
print("Book Details:")
book.display()
print("\nCD Details:")
cd.display()
