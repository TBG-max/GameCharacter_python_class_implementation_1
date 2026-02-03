# module.py

class GameCharacter:
    def __init__(self, name, power, toughness):
        self.name = name
        self.power = power
        self.toughness = toughness
        self.health = 100

    def attack(self):
        return f"{self.name} attacks with power {self.power}!"

    def take_damage(self, amount):
        self.health -= (amount // self.toughness)
        return f"{self.name} takes {amount} damage."

    def heal(self, amount):
        self.health += amount
        return f"{self.name} heals {amount} health."

    def get_status(self):
        return f"-----------------\n{self.name} | Health: {self.health} | Power: {self.power} | Toughness: {self.toughness}\n------------------------------"
