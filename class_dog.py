class Dog:
    """first attempt to model a dog"""

    def __init__(self, name, age, color, breed):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
        self.color = color
        self.breed = breed
        self.objects_sniffed = 0

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"A {self.color} {self.age}-year-old {self.breed} named {self.name}"
        return long_name.title()

    def sniff_count(self):
        """Print a statement showing how many things the dog has sniffed"""
        print(f"{self.name} has sniffed {self.objects_sniffed} things.")

    def update_sniff_count(self, sniffs):
        """
        Set the objects_sniffed to the given value
        Reject the change if it attempts to reduce the number
        """
        if sniffs >= self.objects_sniffed:
            self.objects_sniffed = sniffs
        else:
            print(f"{self.name} cannot un-sniff that which has been sniffed!")


"""
my_dog = Dog('Obby','4','harlequin','spaniel')
my_dog.update_sniff_count(23)
my_dog = Dog('Obby','4')

print(f"My dog's name is {my_dog.name}!")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()
"""


class Puppy(Dog):
    """Represent aspects of a dog, specific to puppies"""

    def __init__(self, name, age, color, breed):
        """Initialize attributes of the parent class"""
        super().__init__(name, age, color, breed)

    def get_age_in_weeks(self):
        """Replace a less-specific years age with a more-specific weeks age."""
        age_in_weeks = self.age * 72
        return age_in_weeks




# The child class needs to be called in the same file as the parent.
# The first step is to call the parent methods in super() for the child to inherit.
# After that you can describe child-specific methods!
# NO NEW ATTRIBUTES. The parent class must hold all attributes its child classes will need.

my_puppy = Puppy('Ash', .31, 'blue', 'spaniel')
print(my_puppy.get_descriptive_name())
print(my_puppy.get_age_in_weeks())