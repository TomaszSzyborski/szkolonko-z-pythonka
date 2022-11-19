from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
# @dataclass_json
@dataclass
class SimpleJsonExample:
    int_field: int

if __name__ == '__main__':
    simple_json = SimpleJsonExample(1)
    # Encoding to a (JSON) string
    print(f"{simple_json.to_json()=}")
    print(f"{type(simple_json.to_json())=}")
    # Encoding to a (JSON) dict

    print(f"{simple_json.to_dict()=}")
    print(f"{type(simple_json.to_dict())=}")

    # Decoding from JSON. Note the input is a string, not a dictionary.
    example_from_json = SimpleJsonExample.from_json('{"int_field": 5}')
    print(example_from_json)
    print(type(example_from_json))
    # Decoding from a (JSON) dict
    example_from_json = SimpleJsonExample.from_dict({'int_field': 1})  # SimpleExample(1)
    print(example_from_json)
    print(type(example_from_json))
    print(example_from_json.int_field)
    print(example_from_json.int_field)
