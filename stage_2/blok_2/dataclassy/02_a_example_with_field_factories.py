import logging
from dataclasses import dataclass, field

from utils.fake_factory import fake

logging.basicConfig()
logging.root.setLevel(logging.INFO)

@dataclass
class Person:
    name: str = field(default_factory=fake.first_name)
    street: str = field(default_factory=fake.street_address)
    ssn: str = field(default_factory=fake.ssn)
    city: str = field(default_factory=fake.city)
    email: str = field(default_factory=fake.email)
    books: list[str] = field(default_factory=list)
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self):
        self._search_string = f"{self.__dict__}"

    def matches_description(self, string):
        logging.debug(self._search_string)
        return string in self._search_string


# @dataclass(frozen=True)
@dataclass(frozen=False)
class FrozenPerson:
    name: str = field(default_factory=fake.first_name)
    street: str = field(default_factory=fake.street_address)
    ssn: str = field(default_factory=fake.ssn)
    city: str = field(default_factory=fake.city)
    email: str = field(default_factory=fake.email)
    books: list[str] = field(default_factory=list)
    id: str = field(default_factory=fake.random_int, init=False)


if __name__ == '__main__':
    crowd = []
    for _ in range(1000):
        crowd.append(Person())
    person = Person(name="David", street="33 Arrows", ssn=fake.ssn(), city=fake.city(), email=fake.email())
    print(person)

    print(crowd[:5])
    davids = [person for person in crowd if person.name == "David"]
    print(f"We have {len(davids)} Davids.")
    david = davids[0]
    print(david)

    print("#" * 120)

    david = FrozenPerson(name="David", street="33 Arrows", ssn=fake.ssn(), city=fake.city(), email=fake.email())
    print(david)
    print(david.id)
    david.id = 456
    print(david.id)
    david.id = None
    print(david.id)
    print(f"And now we just got Dav. {david=}")
