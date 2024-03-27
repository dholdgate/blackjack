import stack


def main():
    deck = stack.Stack()
    assign_new_deck(deck)
    return None


def assign_new_deck(deck: stack.Stack) -> None:
    suits = {"Hearts", "Clubs", "Diamonds", "Spades"}
    values = {"A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"}

    for suit in suits:
        for value in values:
            deck.push({suit, value})

    return
