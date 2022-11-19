import logging
from dataclasses import dataclass, field

from utils.fake_factory import fake

logging.basicConfig()
logging.root.setLevel(logging.INFO)


@dataclass(order=True)
class RPGCharacter:
    sort_index: int = field(init=False, repr=False)
    name: str
    profession: str
    strength: int = 5
    intelligence: int = 5
    agility: int = 5

    def __post_init__(self):
        object.__setattr__(self, 'sort_index', self.strength)


if __name__ == '__main__':
    dwarf = RPGCharacter("Gimli", "Warrior", strength=10)
    hobbit = RPGCharacter("Sam Gamgee", "Gardener", strength=5)
    gollum = RPGCharacter("Gollum", "Gollum", 4)
    gandalf = RPGCharacter("The Grey Wizard", "Wizard", agility=8, intelligence=10)

    for character in [dwarf, hobbit, gollum, gandalf]:
        print(character)
        
    print(f"is dwarf better than hobbit?: {dwarf > hobbit}")
    print(f"is gollum worse than hobbit?:{ gollum < hobbit}")
    print(f"is dwarf better than gollum?: {dwarf > gollum}")
    print(f"is gandalf worse than dwarf?: {gandalf < dwarf}")
