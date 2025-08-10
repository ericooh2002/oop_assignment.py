# Polymorphism Challenge - Activity 2
# Author: Eric Kimeu
# Description:
# Demonstrates polymorphism with different classes having the same method but different behavior.

class Vehicle:
    def move(self):
        print("The vehicle moves.")

class Car(Vehicle):
    def move(self):
        print("Driving on the road...")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky...")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water...")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the path...")

if __name__ == "__main__":
    # Create a list of different vehicles
    vehicles = [Car(), Plane(), Boat(), Bicycle()]

    # Loop through and call the move() method
    print("--- Vehicle Movements ---")
    for v in vehicles:
        v.move()
      
