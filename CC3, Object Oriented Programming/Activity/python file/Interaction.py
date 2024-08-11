class ElderDragon:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def is_slain(self):
        return self.hp == 0


class Player:
    def __init__(self, name, attack, weapon):
        self.name = name
        self.attack = attack
        self.weapon = weapon

    def attack_move(self, elder_dragon):
        print("Player:")
        print(f"{self.name} deals {self.attack} damage to {elder_dragon.name} with a {self.weapon}.")
        print()


class Interaction:
    def __init__(self, players, elder_dragon):
        self.players = players
        self.elder_dragon = elder_dragon

    def battle_results(self):
        for player in self.players:
            player.attack_move(self.elder_dragon)
        if self.elder_dragon.is_slain():
            print(f"Elder Dragon {self.elder_dragon.name} has been slain.")
        else:
            print(f"You failed to slay the Elder Dragon {self.elder_dragon.name}.")


players = [
    Player("Tenshioni", 250, "Longsword"),
    Player("Kimiler", 250, "Longsword"),
    Player("Hexactly", 250, "Switch Axe"),
    Player("Eclair", 250, "Charge Blade")
]

elder_dragon = ElderDragon("Fatalis", 1000)

interaction = Interaction(players, elder_dragon)
interaction.battle_results()