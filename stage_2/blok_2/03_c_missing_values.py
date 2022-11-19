from dataclasses import dataclass
from typing import Any

from dataclasses_json import dataclass_json, CatchAll
from dataclasses_json import Undefined

dump_dict = {"endpoint": "some_api_endpoint", "data": {"foo": 1, "bar": "2"}, "undefined_field_name": [1, 2, 3]}


# @dataclass_json(undefined=Undefined.RAISE)
# @dataclass()
# class ExactAPIDump:
#     endpoint: str
#     data: dict[str, Any]
#
#
# dump = ExactAPIDump.from_dict(dump_dict)


# @dataclass_json(undefined=Undefined.EXCLUDE)
# @dataclass()
# class DoNotCareAPIDump:
#     endpoint: str
#     data: dict[str, Any]
#
#
# dump = DoNotCareAPIDump.from_dict(dump_dict)
# print(dump.to_dict())

# @dataclass_json(undefined=Undefined.INCLUDE)
# @dataclass()
# class UnknownAPIDump:
#     endpoint: str
#     data: dict[str, Any]
#     unknown_things: CatchAll
#
# dump = UnknownAPIDump.from_dict(dump_dict)
# print(dump.to_dict())