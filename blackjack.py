'''BlackJack Game'''
from random import *

class Game(object):
    '''This is an adapted version of the card game blackjack, its rules are
modified from the original version of the game. The goal of the game is to
win from the dealer, therefore get closer from 21 points than your rival'''

    # Defining the deck of cards
    cards_names = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Q', 'J', 'K')
    cards_suits = ('heart', 'diamond', 'spade', 'club')
    cards = []

    # Building each card assigned to its value in the game  
    for name in cards_names:
        for suit in cards_suits:
            try:
                num = int(name)
            except ValueError:
                cards.append([name, suit, 10])
            else:
                cards.append([name, suit, num])

    # Presserving the deck of cards
    cards_default = cards.copy()

    def __init__(self):
        '''Initializing attributes regarding the player and dealer's cards and points'''
        self.player_cards = []
        self.dealer_cards = []
        self.player_count = 0
        self.dealer_count = 0
        self.main()

    def introduce_game(self):
        '''This method introduces the game to the user, thus indicating the rules'''
        self.message = '''Welcome to the simplified blackjack, the only thing you need to do is beat
the dealer. It's very simply, you just need to reach as close as you can 21
points, the dealer will try the same. The one who gets closest wins. If you
go beyond 21 points you'll loose, unless the dealer does the same; in this case
it will be declared a draw. Enjoy the game!\n'''
        print(self.message)

    def pick_card(self, is_player = True):
        '''This method chooses a card from the deck randomly'''
        if is_player:
            self.is_player = is_player
            continue_playing = bool(int(input("Do you want a new card? (1 - Yes / 0 - No)")))
            if not continue_playing:
                return False, [0, 0]

        card_taken = choice(self.cards)
        if is_player:
            print("Card: %s -> %s"%(card_taken[0], card_taken[1]))
        self.cards.remove(card_taken)
        return True, card_taken

    def check_winner(self):
       '''This method check who won the game: dealer or player'''
       print("The player count is %i and the dealer count is %i"%(self.player_count, self.dealer_count))
       if self.player_count > 21 and self.dealer_count > 21:
           print("It is a draw!\n")
       elif (self.player_count > 21 and self.dealer_count < 21) or (21-self.player_count  > 21-self.dealer_count):
           print("Dealer won!\n")
       elif (self.dealer_count > 21 and self.dealer_count < 21) or (21-self.player_count  < 21-self.dealer_count):
           print("You won!\n")

    def main(self):
        '''This is the main method, it calls other methods to run the game'''

        self.introduce_game()
        continue_playing = True

        while continue_playing:

            # Reseting attributes
            self.player_cards = []
            self.dealer_cards = []
            self.player_count = 0
            self.dealer_count = 0
            self.cards = self.cards_default.copy()

            # This loop check if the player wants to keep picking cards
            # and perform the sum of the points (dealer and player)
            while True:
                card_pick_player = self.pick_card()
                if not card_pick_player[0]:
                    break
                else:
                    self.player_cards.append(card_pick_player[1])
                    card_pick_dealer = self.pick_card(False)
                    self.dealer_cards.append(card_pick_dealer[1])
                    self.player_count += card_pick_player[1][2]
                    self.dealer_count += card_pick_dealer[1][2]

            self.check_winner()
            continue_playing = bool(int(input("Do you want to play again? (1 - Yes / 0 - No)")))		

if __name__ == '__main__':
    blackjack = Game()
    help(Game)
