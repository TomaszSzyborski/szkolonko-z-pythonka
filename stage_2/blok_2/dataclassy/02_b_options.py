import logging
from dataclasses import dataclass, field

from utils.fake_factory import fake

logging.basicConfig()
logging.root.setLevel(logging.INFO)


@dataclass(frozen=False,  # immutable
           kw_only=True,  # keywords in initializer ONLY
           match_args=True,  # structural pattern matching
           slots=True)  # performance boost, lock class fields - class is unmodifiable
class Person:
    name: str = field(default_factory=fake.first_name)
    street: str = field(default_factory=fake.street_address)
    ssn: str = field(default_factory=fake.ssn)
    city: str = field(default_factory=fake.city)
    email: str = field(default_factory=fake.email)
    books: list[str] = field(default_factory=list)
    id: str = field(default_factory=fake.random_int, init=False)


if __name__ == '__main__':
    david = Person(name="David", street="33 Arrows", ssn=fake.ssn(), city=fake.city(), email=fake.email())
    # david = Person("David", "33 Arrows", fake.ssn(), fake.city(), fake.email())
    print(david)
    print(david.id)
    david.id = 456
    print(david.id)
    print(david.__dict__["name"])
