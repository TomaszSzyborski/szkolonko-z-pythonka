from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from utils.fake_factory import fake


@dataclass_json
@dataclass(frozen=True)
class Minion:
    name: str


@dataclass_json
@dataclass(frozen=True)
class Boss:
    minions: list[Minion]


boss = Boss([Minion('evil minion'), Minion('very evil minion')])
print(boss)
boss_json = """
{
    "minions": [
        {
            "name": "evil minion"
        },
        {
            "name": "very evil minion"
        }
    ]
}
""".strip()

assert boss.to_json(indent=4) == boss_json
assert Boss.from_json(boss_json) == boss


@dataclass_json
@dataclass(frozen=True)
class Minion:
    name: str
    hp: int = field(default_factory=lambda: fake.pydecimal(positive=True, right_digits=0, min_value=5, max_value=10))
    colour: str = field(default_factory=fake.color_name)


@dataclass_json
@dataclass(frozen=True)
class Boss:
    minions: list[Minion]
    hp: int = field(default_factory=lambda: fake.pydecimal(positive=True, right_digits=0, min_value=15, max_value=20))


boss = Boss([Minion('evil minion'), Minion('very evil minion')])

print(boss)
