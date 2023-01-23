"""
module docstring
"""
import random
from dataclasses import dataclass, field
from enum import Enum
from typing import Protocol


class Ranks(Enum):
    """
    Enum for the number of ranks.
    """

    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


class Suit(Enum):
    """
    Enum for the suit.
    """

    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4


RANKS: list[str] = "2 3 4 5 6 7 8 9 10 J Q K A".split()
SUITS: list[str] = "♣ ♢ ♡ ♠".split()


class CardComparisonStrategy(Protocol):
    """
    Comparison strategy protocol
    """

    @staticmethod
    def sorting_index(rank: str, suit: str) -> int:
        """
        Return the index of the card with the given rank and suit.

        :param rank: the rank of the card
        :param suit: the suit of the card
        :return: the index of the card with the given rank and suit
        """
        ...


class RankFirstComparisonStrategy:
    """
    Comparison strategy for the rank-first comparison method.
    """

    @staticmethod
    def sorting_index(rank: str, suit: str):
        """
        Return the index of the card with the given rank and suit.

        :param rank: the rank of the card
        :param suit: the suit of the card
        :return: the index of the card with the given rank and suit
        """
        return RANKS.index(rank) * len(SUITS) + SUITS.index(suit)


class SuitFirstComparisonStrategy:
    """
    Comparison strategy for the suit-first comparison method.
    """

    @staticmethod
    def sorting_index(rank: str, suit: str) -> int:
        """
        Return the index of the card with the given rank and suit.

        :param rank: the rank of the card
        :param suit: the suit of the card
        :return: the index of the card with the given rank and suit
        """
        return SUITS.index(suit) * 100 + RANKS.index(rank)


@dataclass(order=True, kw_only=True)
class PlayingCard:
    """
    A playing card.

    :param rank: the rank of the card
    :param suit: the suit of the card
    """

    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str
    comparison_strategy: CardComparisonStrategy = field(
        repr=False, default=RankFirstComparisonStrategy
    )

    def __post_init__(self):
        self.sort_index = self.comparison_strategy.sorting_index(self.rank, self.suit)

    def __str__(self):
        return f"{self.suit}{self.rank}"


def make_french_deck(
    comparison_strategy: CardComparisonStrategy|None = None,
) -> list[PlayingCard]:
    """
    Return a list of playing cards with the given comparison strategy.

    :param comparison_strategy: the comparison strategy
    :return: a list of playing cards with the given comparison strategy
    """
    if comparison_strategy is None:
        comparison_strategy = RankFirstComparisonStrategy()
    return [
        PlayingCard(rank=rank, suit=suit, comparison_strategy=comparison_strategy)
        for suit in SUITS
        for rank in RANKS
    ]


@dataclass
class Deck:
    """
    A deck of cards.
    """
    cards: list[PlayingCard] = field(default_factory=make_french_deck)

    def __repr__(self):
        cards = ", ".join(f"{c!s}" for c in self.cards)
        return f"{self.__class__.__name__}({cards})"


if __name__ == "__main__":
    queen_of_hearts = PlayingCard(rank="Q", suit="♡")
    ace_of_spades = PlayingCard(rank="A", suit="♠")
    print(queen_of_hearts)
    print(ace_of_spades)
    print(f"{ace_of_spades > queen_of_hearts=}")
    ten_of_clubs = PlayingCard(rank="10", suit="♣")
    two_of_clubs = PlayingCard(rank="2", suit="♣")
    print(ten_of_clubs)
    print(two_of_clubs)
    print(f"{ten_of_clubs > two_of_clubs=}")
    deck = Deck()
    french_deck = make_french_deck(RankFirstComparisonStrategy)
    random.shuffle(french_deck)
    deck = Deck(french_deck)
    print(deck)
    deck = Deck(sorted(french_deck))
    print(deck)
