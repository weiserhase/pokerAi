#from poke.game import CardDeck

from poker.game import CardDeck


class Outcome:
    def __init__(self, cards: CardDeck):
        self.value: int = 0
        pass


class HighCard(Outcome):
    def __init__(self, cards: CardDeck):
        pass


class Pair(Outcome):
    def __init__(self, cards: CardDeck):
        pass


class Triple(Outcome):
    def __init__(self, cards: CardDeck):
        pass


class Straight(Outcome):
    def __init__(self, cards: CardDeck):
        pass


class Flush(Outcome):
    def __init__(self, cards: CardDeck):
        pass


class Union:
    def __init__(self, out0: Outcome, out1: Outcome):
        pass


def outcome(cards: CardDeck) -> list[Outcome]:
    return list(Outcome(cards))
