from poker.combinations import Outcome
import numpy as np


def get_name(value: int) -> str:
    # TODO Implement
    return str(value)


def default_card_deck() -> "CardDeck":
    # TODO Implement
    return CardDeck([])


class Card:
    def __init__(self, value):
        self.value = value
        self.name = get_name(value)


class CardDeck:
    def __init__(self, cards: list[Card]):
        self.cards: list[Card] = cards

    def get_combinations(self) -> list[Outcome]:
        # TODO replace with actual evaluation
        return [Outcome(CardDeck(self.cards))]

    @property
    def length(self) -> int:
        return len(self.cards)


class Player:
    def __init__(self, name, cards: CardDeck):
        self.name = name
        self.cards = cards
        self.combinations: list[Outcome]

    def update_hand(self, cards: CardDeck):
        self.cards = cards
        self.cards.get_combinations()


class Game:
    def __init__(self, card_deck: CardDeck):
        self.card_stack = card_deck
        self.table: list[Player] = []  # player map
        self.active_cards: CardDeck = CardDeck([])

    def hand_player(self):
        self.active_cards = CardDeck([])
        if self.card_stack.length <= len(self.table)*2:
            self.card_stack = default_card_deck()
        for player in self.table:
            pick = [np.random.choice(self.card_stack.cards, replace=True)
                    for i in range(2)]
            player.update_hand(pick)

    def draw_card(self):
