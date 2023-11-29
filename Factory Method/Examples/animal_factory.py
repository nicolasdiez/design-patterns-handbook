from abc import ABC, abstractmethod
from enum import Enum

# Step 0: Create an enumeration for animal types
class AnimalType(Enum):
    DOG = "Dog"
    CAT = "Cat"
    FISH = "Fish"

# Step 1: Create an abstract Animal class
class Animal(ABC):
    
    def __init__(self, context: dict):
        self.name = context["name"]
        self.age = context["age"]
        
    @abstractmethod
    def get_info(self) -> str:
        pass

# Step 2: Create concrete animal classes
class Dog(Animal):
    
    def __init__(self, context: dict):
        super().__init__(context)

    def get_info(self) -> str: 
        return f"I am a {AnimalType.DOG.value} called {self.name}, and I am {self.age} years old."

class Cat(Animal):
#    def __init__(self, context: dict):
#        super().__init__(context['name'], context['age'])

    def get_info(self) -> str:
        return "I am a {} called {}, and I am {} years old.".format(AnimalType.CAT.value, self.name, self.age)

class Fish(Animal):
#    def __init__(self, context: dict):
#        super().__init__(context['name'], context['age'])

    def get_info(self) -> str:
        info = "I am a {} called {}, and I am {} years old.".format(AnimalType.FISH.value, self.name, self.age)
        return info

# Step 3: Create an AnimalFactory class
class AnimalFactory:
    def create_animal(self, animal_type: AnimalType, context: dict) -> Animal:
        # Implement the logic to create an animal based on the animal_type parameter and context data
        if animal_type == AnimalType.DOG:
            return Dog(context)
        if animal_type == AnimalType.CAT:
            return Cat(context)        
        if animal_type == AnimalType.FISH:
            return Fish(context)
        else:
            raise ValueError(f"Invalid animal type: {animal_type}")
            
# Step 4: Test the AnimalFactory class
def main():
    animal_factory = AnimalFactory()

    # Test the AnimalFactory by creating different types of animals and passing context data
    context = {"name": "Perrito", "age": 14}
    dog = animal_factory.create_animal(AnimalType.DOG, context)
    print(dog.get_info())
    
    context = {"name": "Gatito", "age": 3}
    cat = animal_factory.create_animal(AnimalType.CAT, context)
    print(cat.get_info())
    
    context = {"name": "Pececito", "age": 1}
    fish = animal_factory.create_animal(AnimalType.FISH, context)
    print(fish.get_info())

if __name__ == "__main__":
    main()
