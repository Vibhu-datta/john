from deck import Deck

values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 1}

high_values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11}

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def add_card(self, new_card):
        self.all_cards.append(new_card)

    def show(self):
        print(f"Player {self.name} has:")
        for card in self.all_cards:
            print(card.__str__())

    def hit_or_stand(self):
        response = input(f"player {self.name} would you like to hit or stand(answer with 'h' or 's')")
        return response

    def is_busted(self):
        """Returns true if the hand is busted"""
        value = 0
        for card in self.all_cards: 
            value += values[card.rank]

        if value > 21:
            return True
        else:
            return False
        
    def is_blackjack(self):
        """Returns true if the hand is a blackjack"""
        value = 0
        for card in self.all_cards: 
            value += high_values[card.rank]

        if value == 21:
            return True
        else:
            return False

    def value(self):
        """Returns value for final comparison"""
        value = 0
        for card in self.all_cards: 
            value += values[card.rank]
        # find the number of aces
        num_aces = 0
        for card in self.all_cards:
            if card.rank == "Ace":
                num_aces += 1

        for i in range(num_aces):
            if value + 10 <= 21:
                value += 10
        # loop through, if ad
        # ding 10, won't bust, then add 10

        return value


def game():
    player_one = Player("One")
    player_two = Player("Two")
    my_deck = Deck()
    my_deck.shuffle()

    # deal two cards player and computer
    player_one.add_card(my_deck.deal_one())
    player_one.add_card(my_deck.deal_one())
    player_two.add_card(my_deck.deal_one())

    # show player their cards and computer's first card
    player_one.show()
    player_two.show()
    if player_one.is_blackjack():
        print("Blackjack!")
    else:
        while True :
            response = player_one.hit_or_stand()
            if response == "h":
                player_one.add_card(my_deck.deal_one())
                player_one.show()
                if player_one.is_busted():
                    print("You went bust!, player two wins")
                    return    
            else:
                break
    player_two.add_card(my_deck.deal_one())
    player_two.show()
    if player_two.is_blackjack():
        print("Blackjack!")
    else:
        while True :
            response = player_two.hit_or_stand()
            if response == "h":
                player_two.add_card(my_deck.deal_one())
                player_two.show()
                if player_two.is_busted():
                    print("You went bust!, player one wins")
                    return
            else:
                break
    #compare cards and declare winner
    if player_one.is_blackjack() and player_two.is_blackjack():
        print("Push")
    elif player_one.is_blackjack():
        print("Player one wins")
    elif player_two.is_blackjack():
        print("Player two wins")
    else:
        if player_one.value() > player_two.value():
            print("Player one wins")
        elif player_one.value() < player_two.value():
            print("Player two wins")
        else:
            print("Push")


if __name__ == "__main__":
    game()