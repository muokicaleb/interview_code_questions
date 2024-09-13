"""
I like playing poker, but I need to improve at shuffling cards.

Here is my shuffling method :

I take the card from the top to start a second pile.
I take the next card from the top of the pile and put it under the second pile.
I take the next card from the top of the pile and put it on top of the second pile.
I repeat the last two steps until no card is in the first pile.
Given the initial pile of cards, can you guess the order after my shuffling?

Cards will be defined as strings: “Ace of Spades”, “5 of Hearts”, …
"""

def shuffle_cards(list_cards):
    second_pile = []

    for i, card in enumerate(list_cards):
        if i % 2 == 0:
            second_pile.insert(0, card)
        else:
            second_pile.append(card)
    return second_pile

if __name__ == '__main__':
    list_cards = ["Ace of Spades", "5 of Hearts", "King of Clubs", "8 of Diamonds"]
    print(shuffle_cards(list_cards)) 
            
