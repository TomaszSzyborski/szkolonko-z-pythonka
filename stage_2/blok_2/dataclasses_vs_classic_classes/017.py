# How to compare, but exclude any given field?
# using old style is to create everything from scratch.
# in dataclasses use field(compare=False)
import datetime
from dataclasses import dataclass, field
from time import sleep

from dataclasses_json import dataclass_json, config, LetterCase, Undefined


@dataclass_json(letter_case=LetterCase.CAMEL,
                undefined=Undefined.EXCLUDE)
@dataclass(frozen=True, order=True)
class Comment:
    comment_id: int = field(metadata=config(field_name="id"),
                            compare=False)  # create an alias for the field actually in json
    text: str
    author: str
    created_at: datetime.datetime = field(compare=False)


comment_one = Comment(1, "asd", "Tomasz", datetime.datetime.now())
sleep(3)
comment_two = Comment(2, "zxc", "Tomasz", datetime.datetime.now())
sleep(3)
comment_three = Comment(3, "asd", "Tomasz", datetime.datetime.now())

print(f"{comment_one=}")
print(f"{comment_two=}")
print(f"{comment_one == comment_two=}")

print("=" * 80)

print(f"{comment_one=}")
print(f"{comment_three=}")
print(f"{comment_one == comment_three=}")
