class Monster:
    """first attempt to create an overarching class for monsters"""

    def __init__(self, name, species, size, alignment, subtype=''):
        self.name = name
        self.species = species
        self.type = size
        self.alignment = alignment
        self.subtype = subtype

    def monster_description(self):
        """Call on the monster's attributes to print a description"""
        if self.subtype:
            description = f"{self.name} is a {self.size} {self.alignment} {self.subtype} (subtype of {self.species})."
        else:
            description = f"{self.name} is a {self.size} {self.alignment} {self.species}"
        return description.title()

