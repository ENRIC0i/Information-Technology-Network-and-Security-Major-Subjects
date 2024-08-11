# Programmed by: Abenes, Enrico O.
# Program Date: October 26, 2023
# Program Title: Interaction

class Hero:
    def __init__(self, name, attack_damage = 1000):
        self.name = name
        self.attack_damage = attack_damage

    def attack_move(self):
        print("Hero:")
        print("Hero ", self.name, " deals ", str(self.attack_damage), " damage to Demon Lord.")
        print()

    def cherish(self, mage, warrior, priest):
        print("Hero ", self.name, "cherish his moments, within 10 years of their expedition to slay the Demon Lord, with his party members (Elven Mage ", mage.name, ", Dwarf Warrior ", warrior.name, ", Corrupt Priest ", priest.name, ")")


class Mage:
    def __init__(self, name, ability_power = 900):
        self.name = name
        self.ability_power = ability_power

    def attack_move(self):
        print("Mage:")
        print("Elven Mage ", self.name, " deals", str(self.ability_power), "ability damage to Demon Lord.")
        print()


class Warrior:
    def __init__(self, name, armor = 600, magic_resist = 600):
        self.name = name
        self.armor = armor
        self.magic_resist = magic_resist

    def tank_move(self):
        print("Warrior:")
        print("Dwarf Warrior ", self.name, " takes 1000 damage from Demon Lord with his ", str(self.armor),
              " Armor and ", str(self.magic_resist), " Magic Resist.")
        print()


class Priest:
    def __init__(self, name, healing_power = 500):
        self.name = name
        self.healing_power = healing_power

    def healing_move(self):
        print("Priest:")
        print("Corrupt Priest ", self.name, " deals 1 damage but heals everyone with ", str(self.healing_power),
              " healing power.")
        print()


class Interaction:
    def __init__(self, hero, mage, warrior, priest):
        self.hero = hero
        self.mage = mage
        self.warrior = warrior
        self.priest = priest

    def overall_action(self):
        self.hero.attack_move()
        self.mage.attack_move()
        self.warrior.tank_move()
        self.priest.healing_move()
        self.hero.cherish(self.mage, self.warrior, self.priest)


hero1 = Hero("Himmel")
mage1 = Mage("Frieren")
warrior1 = Warrior("Eisen")
priest1 = Priest("Heiser")

interaction = Interaction(hero1, mage1, warrior1, priest1)

interaction.overall_action()