# OOP Assignment
# Author: Eric Kimeu
# Description:
# 1. Create a class with attributes and methods using a constructor.
# 2. Add inheritance to demonstrate polymorphism.

# ---------- Part 1: Main Class ----------
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours

    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

    def charge(self):
        print(f"{self.brand} {self.model} is charging... Battery full!")

    def __str__(self):
        return f"{self.brand} {self.model} - Battery: {self.battery_life} hrs"


# ---------- Part 2: Inheritance & Polymorphism ----------
class Animal:
    def move(self):
        print("The animal moves in some way.")

class Dog(Animal):
    def move(self):
        print("The dog runs.")

class Bird(Animal):
    def move(self):
        print("The bird flies.")

class Fish(Animal):
    def move(self):
        print("The fish swims.")


# ---------- Testing the Classes ----------
if __name__ == "__main__":
    # Create Smartphone objects
    phone1 = Smartphone("Samsung", "Galaxy S24", 24)
    phone2 = Smartphone("Apple", "iPhone 15", 20)

    print(phone1)
    phone1.make_call("+254712345678")
    phone2.charge()

    print("\n--- Polymorphism Example ---")
    animals = [Dog(), Bird(), Fish()]
    for animal in animals:
        animal.move()
