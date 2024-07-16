#Write a program that has class Cars.
#Create two objects and set Car1 to be a red convertible with
#price 10 lakhs and name Pugo.
#Car2 to be a blue sedan named Mavo worth 6 lakhs
class Cars:
    def __init__(self, name, color, car_type, price):
        self.name = name
        self.color = color
        self.car_type = car_type
        self.price = price

# Creating Car1 and Car2 objects
car1 = Cars(name="Pugo", color="red", car_type="convertible", price=1000000)  # 10 lakhs = 1,000,000
car2 = Cars(name="Mavo", color="blue", car_type="sedan", price=600000)  # 6 lakhs = 600,000

# Accessing and printing the attributes of Car1 and Car2
print(f"Car1: {car1.name} - Color: {car1.color} - Type: {car1.car_type} - Price: {car1.price} lakhs")
print(f"Car2: {car2.name} - Color: {car2.color} - Type: {car2.car_type} - Price: {car2.price} lakhs")
