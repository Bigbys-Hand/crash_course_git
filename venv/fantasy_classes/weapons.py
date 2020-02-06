class Melee_Weapon:
    """First attempt to create an overarching class for melee weapons"""

    def __init__(self, magic_bonus, cost, weight, material, wield, category, type, damage_dice, size, enhancement=''):
        self.magic_bonus = magic_bonus
        self.cost = cost
        self.weight = weight
        self.material = material
        self.wield = wield
        self.category = category
        self.type = type
        self.damage_dice = damage_dice
        self.size = size
        self.enhancement = enhancement
        """category is for longsword/quarterstaff/kukri, type is for simple/martial/exotic"""