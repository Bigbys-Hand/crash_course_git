class Restaurant:
    """Following the exercise on pg.162"""

    def __init__(self, name, cuisine):
        """Initialize restaurant name and cuisine type attributes"""
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Prints name and cuisine type"""
        print(f"The restaurant is named {self.name} and it serves {self.cuisine} food")

    def open_restaurant(self):
        """Prints a message indicating the restaurant is open"""
        print(f"{self.name} is open! Grab yourself a table.")
