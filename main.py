# Base class for a Superhero
class Superhero:
    def __init__(self, name, superpower, alias):
        # Encapsulation: These attributes are considered private
        self.__name = name  # private attribute
        self.__superpower = superpower  # private attribute
        self.alias = alias  # public attribute

    # Public method to get the private name
    def get_name(self):
        return self.__name

    # Public method to get the private superpower
    def get_superpower(self):
        return self.__superpower

    # Method to display the superhero's info
    def display_info(self):
        return f"Superhero: {self.alias} \nReal Name: {self.get_name()} \nSuperpower: {self.get_superpower()}"

    # Method to perform an action
    def use_superpower(self):
        return f"{self.alias} uses {self.__superpower}!"


# Inherited class representing a specific superhero (e.g., a Flying Superhero)
class FlyingSuperhero(Superhero):
    def __init__(self, name, superpower, alias, flight_speed):
        # Inherit attributes from the base class
        super().__init__(name, superpower, alias)
        self.flight_speed = flight_speed  # additional attribute unique to FlyingSuperhero

    # Overriding the method to show additional behavior (polymorphism)
    def use_superpower(self):
        # Adding flight-specific functionality
        return f"{self.alias} flies at {self.flight_speed} speed using {self.get_superpower()}!"

    # Method to display flying superhero's info
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info} \nFlight Speed: {self.flight_speed}"


# Creating objects of the classes
hero1 = Superhero("Bruce Wayne", "Detective Skills", "Batman")
hero2 = FlyingSuperhero("Clark Kent", "Super Strength and Flight", "Superman", "Mach 3")

# Displaying their information
print(hero1.display_info())  # Calling method from the base class
print(hero1.use_superpower())  # Calling method from the base class

print("\n---")

print(hero2.display_info())  # Calling overridden method from the derived class
print(hero2.use_superpower())  # Calling overridden method from the derived class
