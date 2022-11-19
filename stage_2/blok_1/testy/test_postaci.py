from pytest import fixture
from pytest import mark
from stage_2.blok_1.testy.rpg_characters_inheritance import Villain, CharacterState as cs


@fixture
def villain():
    return Villain("Złodupiec", 100, 23)


def test_character_name(villain):
    assert villain.name == "Złodupiec"


@mark.parametrize("hp, expected_state",
                  [(1, cs.ALIVE), (1000, cs.ALIVE), (-1, cs.DEAD), (0, cs.ALIVE)]
                  )
def test_bee_gees(villain, hp, expected_state):
    villain.hp = hp
    assert villain.state == expected_state
