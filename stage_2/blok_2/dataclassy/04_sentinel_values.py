
import dataclasses
from dataclasses import field
from typing import Optional, cast

from dataclasses_json import dataclass_json, config, LetterCase

SENTINEL = cast(object, None)

########################

@dataclass_json
@dataclasses.dataclass
class Nested:
    x: str = field(default="some_String")
    y: dict = field(default=None)


@dataclass_json
@dataclasses.dataclass
class Something:
    a: int
    b: int
    c: Optional[int] = field(default=SENTINEL, metadata=config(exclude=lambda x: x is SENTINEL))
    d: Optional[Nested] = field(default_factory=lambda: Nested("1", {"myKey": "MyValue"}))


if __name__ == '__main__':
    s = Something(1, 2)
    print(s)
    print(s.to_json())
    s = Something(1, 2, 3)
    print(s)
    print(s.to_json())
    s = Something(1, 2, d=Nested(y={"custom_key": "custom_value"}))
    print(s)
    print(s.to_json())