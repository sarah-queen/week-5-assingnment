# Base class for any moving entity
class MovingEntity:
    def move(self):
        pass  # A generic move method that will be overridden

# Car class inheriting from MovingEntity
class Car(MovingEntity):
    def move(self):
        print("Driving 🚗")

# Plane class inheriting from MovingEntity
class Plane(MovingEntity):
    def move(self):
        print("Flying ✈️")

# Dog class inheriting from MovingEntity
class Dog(MovingEntity):
    def move(self):
        print("Running 🐕")

# Fish class inheriting from MovingEntity
class Fish(MovingEntity):
    def move(self):
        print("Swimming 🐟")

# Creating objects of each class
car = Car()
plane = Plane()
dog = Dog()
fish = Fish()

# Demonstrating polymorphism: calling move() on each object
car.move()   # Output: Driving 🚗
plane.move()  # Output: Flying ✈️
dog.move()    # Output: Running 🐕
fish.move()   # Output: Swimming 🐟
