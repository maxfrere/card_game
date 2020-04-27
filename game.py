# Packages import
import random


#Create classes
class Card():
    def __init__(self, color, value):
        self.color = color
        self.value = value
    name_color = ['clover', 'square', 'heart', 'spades']
    #We could've used here a dictionary
    #'None' makes each index equal to its corresponding value (avoid confusion)
    name_value = [None, 'ace', '2', '3', '4', '5', '6', '7',
                        '8', '9', '10', 'jack', 'queen', 'king']
# Respresent our object as a string with __str__
    def __str__(self):
         return '%s of %s' % (Card.name_value[self.value],
                              Card.name_color[self.color])

##Comparaison : use the __lt__ instead of <
    def __lt__(self, other):
        # Check the colors
        if self.color < other.color: return True
        if self.color > other.color: return False

        # les couleurs sont identiques... vérifier les valeurs
        return self.value < other.value

#Create a class deck and define all the actions that it as functions
class Deck:

    def __init__(self):
        self.cards = []
        for color in range(4):
            for value in range(1, 14):
                card = Card(color, value)
                self.cards.append(card)

    def __str__(self):
       result = []
       for card in self.cards:
        result.append(str(card))
       return '\n'.join(result)

   ##Cards Distribution
    #Pick and disturb cards starting from the last one
    def pick_card(self):
        return self.cards.pop()

    #Place cards in the hand
    def place_card(self, hand, num):
        for i in range(num):
            hand.add_card(self.pick_card())

    #Add cards
    def add_card(self, card):
        self.cards.append(card)

    #Shuffle cards
    def mix_card(self):
        random.shuffle(self.cards)

    #Sort cards from the weakest card to the strongest
    def sort_card(self):
        self.cards.sort()

#We'll create the class Hand that inherits the class Card
class Hand(Deck):
    def __init__(self, hand_id = ''):
        self.cards = []
        self.hand_id = hand_id

def play_turn(turn_id):
    hand = Hand(turn_id)
    deck.place_card(hand, 5)
    hand.sort_card()
    print(turn_id)
    print(hand)


if __name__ == '__main__':
    deck = Deck()
    deck.mix_card()
    turn = 0
    for i in range(10):
        if (i % 2) == 0:
            turn = turn + 1
            play_turn('Player one hand '+str(turn))
        else:
            play_turn('Player two hand '+str(turn))
