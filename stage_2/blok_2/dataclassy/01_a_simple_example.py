import logging
from dataclasses import dataclass, field

from utils.fake_factory import fake

logging.basicConfig()
logging.root.setLevel(logging.INFO)


class ClassicPerson:
    def __init__(self, name, street, ssn, city, email):
        self.name = name
        self.street = street
        self.ssn = ssn
        self.city = city
        self.email = email

    def __str__(self):
        return f"{self.name} etc etc"

    def __post_init__(self):
        self._search_string = f"{self.__dict__}"

    def matches_description(self, string):
        logging.debug(self._search_string)
        return string in self._search_string


@dataclass
class Person:
    name: str
    street: str
    ssn: str
    city: str
    email: str
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self):
        self._search_string = f"{self.__dict__}"

    def matches_description(self, string):
        logging.debug(self._search_string)
        return string in self._search_string


if __name__ == '__main__':
    classic_person = ClassicPerson(fake.first_name(), fake.street_address(), fake.ssn(), fake.city(), fake.email())
    print(classic_person)

    crowd = []
    for _ in range(1000):
        crowd.append(Person(fake.first_name(), fake.street_address(), fake.ssn(), fake.city(), fake.email()))
    person = Person(name="David", street="33 Arrows", ssn=fake.ssn(), city=fake.city(), email=fake.email())
    print(person)
    print(person._search_string)  # just for academic purposes

    print(crowd[:5])
    davids = [person for person in crowd if person.matches_description("David")]
    print(f"We have {len(davids)} Davids.")
    print(f"But I'm sorry Dave, I cannot let you do that.")
