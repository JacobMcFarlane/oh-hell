# Representation for a group of cards
import random


class Pile:
    def __init__(self, cards=[]):
        self.cards = cards

    def draw_cards(self, n):
        # Get n random cards from top of deck
        if len(self.cards) < n:
            raise Exception(f"Can't draw {n} cards, only {len(self.cards)} in deck")
        return self.cards[:n]

    def get_extreme_value_card(self, suit, high_or_low="high"):
        suit_values = [card[1] for card in self.cards if card[0] == suit]
        if len(suit_values) == 0:
            return None
        if high_or_low == "high":
            card_val = max(suit_values)
        elif high_or_low == "low":
            card_val = min(suit_values)
        return (suit, card_val)

    def play_card(self, card):
        self.cards.remove(card)
        return card

    def fill_deck(self):
        deck = []
        for i in range(2, 15):
            for suit in ["Hearts", "Spades", "Diamonds", "Clubs"]:
                deck.append((suit, i))
        random.shuffle(deck)
        self.cards = deck

    def play_high_card(self, suite):
        card = self.get_extreme_value_card(suite, "high")
        if card is None:
            return None
        return self.play_card(card)

    def play_low_card(self, suite):
        card = self.get_extreme_value_card(suite, "low")
        if card is None:
            return None
        return self.play_card(card)
