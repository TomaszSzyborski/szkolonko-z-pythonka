from dataclasses import dataclass, field

from dataclasses_json import dataclass_json, LetterCase, config


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Person:
    name: str
    profession_of_choice: str = field(default="QA")


tomasz = Person('tomasz')

# Encoding to JSON
print(tomasz.to_json())
# Decoding from JSON
assert Person.from_json('{"name": "tomasz"}') == tomasz

people_json = [Person(name) for name in ("Sachin", "Sam", "Prasanna", "Dawid", "Ruben")]
people = Person.schema().dumps(people_json, many=True)
print(people)

robert = Person.from_json('{"name": "Robert", "professionOfChoice": "DevOps"}')
print(robert)
robert = Person.from_json('{"name": "Robert", "profession_of_choice": "DevOps"}')
print(robert)