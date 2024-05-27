#Cesar  Murillo
#CIS261
#Deck of Cards

import random

class Cards:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
class Deck:
    def __init__(self):
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.shuffle_deck() 
    
    def shuffle_deck(self):
        self.deck = [Card(rank,suit) for suit in self.suits for rank in self.ranks]
        random.shuffle(self.deck)
        
    def deal_cards(self, numb_cards):
        dealt_cards = self.deck[:num_cards]
        self.deck =self.deck[num_cards:]
        return dealt_cards
    
    def remaining_cards(self):
        return len(self.deck)
    
def main():
    deck = Deck()
    
    print("Welcome To The Card Dealer 3000!\n",
          "I Have Shuffled A Deck of 52 Cards.\n")
    
    while True:
        try:
            num_cards = int(input("How Many Cards Would You Like?: "))
            if num_cards < 1 or num_cards > deck.remaining_cards():
                print(f"Cannot Deal {num_cards} Cards. How Many Cards Would You Like?")
                
            dealt_cards = deck.deal_cards(num_cards)
            print("\nHere Are Your Cards: \n")
            for card in dealt_cards:
                print(card)
        except ValueError:
            print("Please Enter How Many Cards You Would Like.")
            continue
        
        remaining = deck.remaining_cards()
        print(f"\nThere Are {remaining} Cards Left In The Deck.\n")
        print("Good Luck My Friend!\n")
       
        input("Press Any Key To Deal Again...")
        
        if remaining == 0:
            print("There Are No More Cards To Deal. Thank You For Playing!")
            break

if __name__ == "__main__":
    main()
          
