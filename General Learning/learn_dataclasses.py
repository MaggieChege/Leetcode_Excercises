from dataclasses import dataclass

# documentated Resources: https://www.notion.so/Python-Resources-9de20e8586264545bf102228311e6e1b?p=03a045f00abd4ccfb79a9281a81c1305&pm=s


@dataclass
class DataClassCard:
    rank: str
    suit: str


class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}" f"(rank={self.rank!r}, suit={self.suit!r})"

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.rank, self.suit) == (other.rank, other.suit)


# Named Tuple

from collections import namedtuple

NamedTupleCard = namedtuple("NamedTupleCard", ["rank", "suit"])


# attrs

import attr


@attr.s
class AttrsCard:
    rank = attr.ib()
    suit = attr.ib()


@dataclass
class Locationinfo:
    name: str
    lon: float
    lat: float


from math import asin, cos, radians, sin, sqrt


@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

    def distance_to(self, other):
        r = 6371  # earth Redius in KM
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (
            sin((phi_2 - phi_1) / 2) ** 2
            + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2) ** 2
        )

        return 2 * r * asin(sqrt(h))


if __name__ == "__main__":
    print(DataClassCard("Queen", "Hearts"))
    card = RegularCard("Queen", "Hearts")
    print(card)
    print(repr(card))
    queen_of_hearts = NamedTupleCard("Queen", "Hearts")
    print(queen_of_hearts.rank)
    print(AttrsCard("Q", "Hearts"))
    # locationinfo

    pos = Locationinfo("Oslo", 10.8, 59.0)
    vancouver = Position("Vancouver", -123.1, 49.4)
    oslo = Position("Oslo", 10.8, 59.0)
    print(pos)
    print(f"{pos.name} is at {pos.lat}N, {pos.lon}E", "--> location info")
    print(oslo.distance_to(vancouver), "----> Distance from oslo to Vancouver")
