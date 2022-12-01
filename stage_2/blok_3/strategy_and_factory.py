"""
module docstring
"""
import random
from dataclasses import dataclass, field
from enum import StrEnum, Enum
from typing import Protocol


class Rank(Enum):
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
    JACK = "J"
    QUEEN = "Q"
    KING = "K"
    ACE = "A"


class Suit(StrEnum):
    """
    Enum for the suit.
    """

    CLUBS = "♣"
    DIAMONDS = "♢"
    HEARTS = "♡"
    SPADES = "♠"


class CardComparisonStrategy(Protocol):
    """
    Comparison strategy protocol
    """

    @staticmethod
    def sorting_index(rank: Rank, suit: Suit) -> int:
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
    def sorting_index(rank: Rank, suit: Suit):
        """
        Return the index of the card with the given rank and suit.

        :param rank: the rank of the card
        :param suit: the suit of the card
        :return: the index of the card with the given rank and suit
        """
        return list(Rank).index(rank) * len(Suit) + list(Suit).index(suit)


class SuitFirstComparisonStrategy:
    """
    Comparison strategy for the suit-first comparison method.
    """

    @staticmethod
    def sorting_index(rank: Rank, suit: Suit) -> int:
        """
        Return the index of the card with the given rank and suit.

        :param rank: the rank of the card
        :param suit: the suit of the card
        :return: the index of the card with the given rank and suit
        """
        return list(Suit).index(suit) * 100 + list(Rank).index(rank)


@dataclass(order=True, kw_only=True)
class PlayingCard:
    """
    A playing card defined by Rank and suit.
    """

    sort_index: int = field(init=False, repr=False)
    rank: Rank
    suit: Suit
    comparison_strategy: CardComparisonStrategy = field(
        repr=False, default=RankFirstComparisonStrategy
    )

    def __post_init__(self):
        self.sort_index = self.comparison_strategy.sorting_index(self.rank, self.suit)

    def __str__(self):
        return f"{self.suit.value}{self.rank.value}"


def make_french_deck(
        comparison_strategy: CardComparisonStrategy | None = None,
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
        for suit in Suit
        for rank in Rank
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
    queen_of_hearts = PlayingCard(rank=Rank.QUEEN, suit=Suit.HEARTS)
    ace_of_spades = PlayingCard(rank=Rank.ACE, suit=Suit.SPADES)
    print(queen_of_hearts)
    print(ace_of_spades)
    print(f"{ace_of_spades > queen_of_hearts=}")
    ten_of_hearts = PlayingCard(rank=Rank.TEN,
                                suit=Suit.HEARTS,
                                comparison_strategy=SuitFirstComparisonStrategy())
    king_of_clubs = PlayingCard(rank=Rank.KING,
                                suit=Suit.CLUBS)
    print(ten_of_hearts)
    print(king_of_clubs)
    print(f"{ten_of_hearts > king_of_clubs=}")
    print(f"{ten_of_hearts < king_of_clubs=}")
    print(f"{king_of_clubs > ten_of_hearts=}")
    print(f"{king_of_clubs < ten_of_hearts=}")

    print("Suit First Comparison")
    french_deck = make_french_deck(SuitFirstComparisonStrategy)
    random.shuffle(french_deck)
    deck = Deck(french_deck)
    print(deck)
    deck = Deck(sorted(french_deck))
    print(deck)

    print("Rank First Comparison")
    french_deck = make_french_deck(RankFirstComparisonStrategy)
    random.shuffle(french_deck)
    deck = Deck(french_deck)
    print(deck)
    deck = Deck(sorted(french_deck))
    print(deck)
