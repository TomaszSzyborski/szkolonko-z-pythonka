from pytest import fixture
from pytest import mark

from stage_2.blok_1.testy.rpg_characters_inheritance import Villain, CharacterState as cs


@fixture(scope="session", autouse=True)
def example_session():
    print("session start".center(50, "-"))
    yield
    print("session end".center(50, "-"))


@fixture(scope="module", autouse=True)
def example_module():
    print("module start".center(50, "#"))
    yield
    print("module end".center(50, "#"))


@fixture(scope="function", autouse=True)
def example_function():
    print("function start".center(50, "%"))
    yield
    print("function end".center(50, "%"))


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
