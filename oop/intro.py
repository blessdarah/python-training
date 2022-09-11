"""
Introduction to object oriented programming, concepts and termonlogies
Author: Bless Darah
Date: Setp 11, 2022
"""
# Abstraction
# Classess and Objects
# Inheritance
# Encapsulation
# Polymorphism

class Animal:
    def __init__(self, _legs, _name="Bless"):
       self.name = _name
       self.legs = _legs

    def talk(self):
        print("Animal is talking")

    def info(self) -> None:
        print("Name:", self.name)
        print("Legs:", self.legs)


# Inheritance
class Dog(Animal):
    # name, legs, breed
    def __init__(self, name, breed):
        super().__init__(4, name)
        self.breed = breed
        
    def talk(self):
        print(f"{self.name} says whoof whoof!!!")

# Inheritance
class Duck(Animal):
    def __init__(self, _name, _color):
        super().__init__(2, _name)
        self.color = _color

    def talk(self):
        print("Quack-quack")

animal = Animal(0, "snake")
dog = Dog("skipper", "bulldog")
duck = Duck("Donald", "white")


dog.talk()
duck.talk()

