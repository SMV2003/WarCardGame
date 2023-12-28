# Global variables for Card class
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Cards:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


import random


class Deck:
    def __init__(self):
        # creates an empty deck of cards in list form
        self.full_deck = []

        # Adds Cards to the list
        for rank in ranks:
            for suit in suits:
                current_card = Cards(rank, suit)
                self.full_deck.append(current_card)

    def shuffle(self):
        # Shuffles the deck
        random.shuffle(self.full_deck)

    def deal_card(self):
        # removes a card from bottom of the deck
        if not self.full_deck:
            return None
        else:
            return self.full_deck.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def play_hand(self):
        # removes card from top of the players deck(hand)
        if self.hand == []:
            return None
        else:
            return self.hand.pop(0)

    def add_card(self, new_card):
        # Adds card(s) to end of the players deck
        if isinstance(new_card, list):
            self.hand.extend(new_card)
        elif isinstance(new_card, Cards):
            self.hand.append(new_card)

    def __str__(self):
        # returns the name and number of cards player has
        return f'Player {self.name} has {len(self.hand)} cards'


def distribute_cards(player, deck):
    gamer = player
    for _ in range(0, 26):
        card_1 = deck.full_deck.pop(0)
        gamer.add_card(card_1)

    return gamer


def check_empty(player1, player2):
    list1 = player1.hand
    list2 = player2.hand

    if len(list1) == 0:
        return True
    elif len(list2) == 0:
        return True
    else:
        return False


new_deck = Deck()
new_deck.shuffle()
name1 = input('What is your name : ')
name2 = input('What is your name : ')
player1 = Player(name1)
player2 = Player(name2)

player1 = distribute_cards(player1, new_deck)
player2 = distribute_cards(player2, new_deck)

max_consecutive_ties = 10  # Define a threshold for consecutive ties
consecutive_ties = 0  # Initialize the counter
game_round = 0

while not check_empty(player1, player2):
    game_round +=1
    if game_round == 100:
        break
    print(f'\n\nRound {game_round}')
    pcard1 = player1.play_hand()
    print(pcard1)
    if pcard1 is None:
        break

    pcard2 = player2.play_hand()
    print(pcard2)
    if pcard2 is None:
        break

    war_chest = [pcard1, pcard2]

    if pcard1.value > pcard2.value:
        player1.add_card(war_chest)
        print(f'{player1.name} Won the round')
        round_winner = 1
        consecutive_ties = 0  # Reset the counter after a non-tie round
    elif pcard2.value > pcard1.value:
        player2.add_card(war_chest)
        print(f'{player2.name} Won the round')
        round_winner = 1
        consecutive_ties = 0  # Reset the counter after a non-tie round
    elif pcard2.value == pcard1.value:
        for _ in range(0, 5):
            card_from_player1 = player1.play_hand()
            if card_from_player1 is None:
                break
            war_chest.append(card_from_player1)

            card_from_player2 = player2.play_hand()
            if card_from_player2 is None:
                break
            war_chest.append(card_from_player2)

        consecutive_ties += 1  # Increment the counter for consecutive ties

        # Check if consecutive ties threshold has been exceeded
        if consecutive_ties >= max_consecutive_ties:
            print("The game has been tied for too long. Exiting...")
            break  # Exit the loop to prevent getting stuck

if len(player1.hand) == 0 or round_winner == 2:
    print(f'{player2.name} Won the match!')
elif len(player2.hand) == 0 or round_winner == 1:
    print(f'{player1.name} Won the match!')
