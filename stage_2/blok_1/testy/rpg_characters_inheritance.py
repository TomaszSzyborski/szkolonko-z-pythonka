from abc import ABC
from enum import Enum


class Item(ABC):
    def __init__(self, name: str):
        self.name = name


class Weapon(Item):
    def __init__(self, name: str, damage: int):
        super().__init__(name)
        self.damage = damage


class Effect(Enum):
    MANA = "Mana",
    LIFE = "Life"


class CharacterState(Enum):
    ALIVE = "Alive",
    DEAD = "Dead"


class Potion(Item):
    def __init__(self, name, effect: Effect, power: int):
        super().__init__(name)
        self.effect = effect
        self.power = power


class ScrollOfStrength(Item):
    def __init__(self, name, power: int):
        super().__init__(name)
        self.power = power


class Character(ABC):
    def __init__(self, name: str, hp: int, strength: int, weapon: Weapon):
        self.name = name
        self._hp = hp
        self.strength = strength
        self.weapon = weapon
        self.state = CharacterState.ALIVE
        self.inventory: list[Item] = []

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value: int):
        if value <= 0:
            self._hp = 0
            self.state = CharacterState.DEAD
            print(f"{self.name} is slain!")
        else:
            self._hp = value

    def attack(self, target_character):
        print(f"{self.name} attacks {target_character.name}")
        target_character.hp -= (self.strength + self.weapon.damage)

    def put_item_to_inventory(self, item: Item):
        self.inventory.append(item)

    def drink_potion(self, potion: Potion):
        if potion in self.inventory:
            self.inventory.remove(potion)
            if potion.effect == Effect.LIFE:
                self.hp += potion.power


class Hero(Character):
    def __init__(self, name: str, hp: int, strength: int):
        super().__init__(name, hp, strength, Weapon("Leszczynowy Kij", 1))
        self.character_type = "Good"


class Villain(Character):
    def __init__(self, name: str, hp: int, strength: int):
        super().__init__(name, hp, strength, Weapon("Kindżał Rzezi", 17))
        self.character_type = "Evil"


if __name__ == "__main__":
    hero = Hero("Rumcajs", hp=40, strength=4)
    villain = Villain("Villain", hp=100, strength=10)

    print(hero.name, hero.hp, hero.strength)
    print(villain.name, villain.hp, villain.strength)
    minor_healing_potion = Potion("Minor Health Potion", Effect.LIFE, 10)
    hero.put_item_to_inventory(minor_healing_potion)
    villain.attack(hero)

    print(hero.name, hero.hp, hero.strength)
    print(villain.name, villain.hp, villain.strength)

    blood_potion = Potion("Blood Potion", Effect.LIFE, 40)
    hero.put_item_to_inventory(blood_potion)
    hero.drink_potion(blood_potion)

    print(hero.name, hero.hp, hero.strength)
    print(hero.state)

    villain.attack(hero)
    print(hero.name, hero.hp, hero.strength)
    print(hero.state)

    print(villain.name, villain.hp, villain.strength)
    villain.attack(hero)
    print(hero.name, hero.hp, hero.strength)
    print(villain.name, villain.hp, villain.strength)
    print(hero.state)
