import logging
from dataclasses import dataclass, field

from utils.fake_factory import fake

logging.basicConfig()
logging.root.setLevel(logging.INFO)


class ClassicPerson:
    def __init__(self, name=fake.first_name(), street=fake.street_address(),
                 ssn=fake.ssn(), city=fake.city(), email=fake.email()):#, book_list=None):
        self.name = name
        self.street = street
        self.ssn = ssn
        self.city = city
        self.email = email
        # if book_list is None:
        #     self.book_list = []

    def __str__(self):
        return f"{self.name} etc etc"
    
    def __post_init__(self):
        self._search_string = f"{self.__dict__}"

    def matches_description(self, string):
        logging.debug(self._search_string)
        return string in self._search_string

@dataclass
class Person:
    name: str = fake.first_name()
    street: str = fake.street_address()
    ssn: str = fake.ssn()
    city: str = fake.city()
    email: str = fake.email()
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self):
        self._search_string = f"{self.__dict__}"

    def matches_description(self, string):
        logging.debug(self._search_string)
        return string in self._search_string


if __name__ == '__main__':
    classic_person = ClassicPerson()
    print(classic_person)
    for _ in range(10):
        print(ClassicPerson())
    
    crowd = []
    for _ in range(1000):
        crowd.append(Person())
    person = Person(name="David", street="33 Arrows", ssn=fake.ssn(), city=fake.city(), email=fake.email())
    print(person)
    print(person._search_string)  # just for academic purposes

    print(crowd[:5])
    davids = [person for person in crowd if person.matches_description("David")]
    print(f"We have {len(davids)} Davids.")
    print(f"But I'm sorry Dave, I cannot let you do that.")
