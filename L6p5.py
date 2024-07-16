from abc import ABC, abstractmethod

class Fruit(ABC):
    @abstractmethod
    def taste(self):
        pass
    
    @abstractmethod
    def rich_in(self):
        pass
    
class Mango(Fruit):
    def taste(self):
        return "sweet"
    
    def rich_in(self):
        return "Vitamin A"

class Orange(Fruit):
    def taste(self):
        return "Sour"
    
    def rich_in(self):
        return "Vitamin C"

# Instantiate concrete classes
alphanso = Mango()
print(alphanso.taste(), alphanso.rich_in())

orange = Orange()
print(orange.taste(), orange.rich_in())
