import random 
##this is the card object.
class card:
    
    def __init__(self, card_key):
        self.card_name=""
        self.card_value=[]
        self.card_suite=""
        self.card_key=card_key
        self.typenum=0
        self.card_count=0
        
##Deck object is a collection of card objects. Fills out the valus of cards in the deck, there suite, and the value in the card count.
class Deck:
    
    def __init__(self):
        self.standard_deck=[]
        for i in range(1,53):
            self.standard_deck.append(card(i))
        for j in range(1,53):
            if j<14:
                self.standard_deck[j-1].typenum=j
                self.standard_deck[j-1].card_suite="Spades"
                if self.standard_deck[j-1].typenum==1:
                    self.standard_deck[j-1].card_name="Ace"
                    self.standard_deck[j-1].card_value.append(1)
                    self.standard_deck[j-1].card_value.append(11)
                    self.standard_deck[j-1].card_count=-1
                elif self.standard_deck[j-1].typenum==2:
                    self.standard_deck[j-1].card_name="2"
                    self.standard_deck[j-1].card_value.append(2)
                    self.standard_deck[j-1].card_value.append(2)
                    self.standard_deck[j-1].card_count=1
                elif self.standard_deck[j-1].typenum==3:
                    self.standard_deck[j-1].card_name="3"
                    self.standard_deck[j-1].card_value.append(3)
                    self.standard_deck[j-1].card_value.append(3)
                    self.standard_deck[j-1].card_count=1
                elif self.standard_deck[j-1].typenum==4:
                    self.standard_deck[j-1].card_name="4"
                    self.standard_deck[j-1].card_value.append(4)
                    self.standard_deck[j-1].card_value.append(4)
                    self.standard_deck[j-1].card_count=1
                elif self.standard_deck[j-1].typenum==5:
                    self.standard_deck[j-1].card_name="5"
                    self.standard_deck[j-1].card_value.append(5)
                    self.standard_deck[j-1].card_value.append(5)
                    self.standard_deck[j-1].card_count=1
                elif self.standard_deck[j-1].typenum==6:
                    self.standard_deck[j-1].card_name="6"
                    self.standard_deck[j-1].card_value.append(6)
                    self.standard_deck[j-1].card_value.append(6)
                    self.standard_deck[j-1].card_count=1
                elif self.standard_deck[j-1].typenum==7:
                    self.standard_deck[j-1].card_name="7"
                    self.standard_deck[j-1].card_value.append(7)
                    self.standard_deck[j-1].card_value.append(7)
                    self.standard_deck[j-1].card_count=0
                elif self.standard_deck[j-1].typenum==8:
                    self.standard_deck[j-1].card_name="8"
                    self.standard_deck[j-1].card_value.append(8)
                    self.standard_deck[j-1].card_value.append(8)
                    self.standard_deck[j-1].card_count=0
                elif self.standard_deck[j-1].typenum==9:
                    self.standard_deck[j-1].card_name="9"
                    self.standard_deck[j-1].card_value.append(9)
                    self.standard_deck[j-1].card_value.append(9)
                    self.standard_deck[j-1].card_count=0
                elif self.standard_deck[j-1].typenum==10:
                    self.standard_deck[j-1].card_name="10"
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_count=-1
                elif self.standard_deck[j-1].typenum==11:
                    self.standard_deck[j-1].card_name="Jack"
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_count=-1
                elif self.standard_deck[j-1].typenum==12:
                    self.standard_deck[j-1].card_name="Queen"
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_count=-1
                elif self.standard_deck[j-1].typenum==13:
                    self.standard_deck[j-1].card_name="King"
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_count=-1
                    
            elif j<27:
                self.standard_deck[j-1].typenum=j-13
                self.standard_deck[j-1].card_suite="Clubs"
                if self.standard_deck[j-1].typenum==1:
                    self.standard_deck[j-1].card_name="Ace"
                    self.standard_deck[j-1].card_value.append(1)
                    self.standard_deck[j-1].card_value.append(11)
                    self.standard_deck[j-1].card_count=-1
                elif self.standard_deck[j-1].typenum==2:
                    self.standard_deck[j-1].card_name="2"
                    self.standard_deck[j-1].card_value.append(2)
                    self.standard_deck[j-1].card_value.append(2)
                    self.standard_deck[j-1].card_count=1
                elif self.standard_deck[j-1].typenum==3:
                    self.standard_deck[j-1].card_name="3"
                    self.standard_deck[j-1].card_value.append(3)
                    self.standard_deck[j-1].card_value.append(3)
                    self.standard_deck[j-1].card_count=1
                elif self.standard_deck[j-1].typenum==4:
                    self.standard_deck[j-1].card_name="4"
                    self.standard_deck[j-1].card_value.append(4)
                    self.standard_deck[j-1].card_value.append(4)
                    self.standard_deck[j-1].card_count=1
                elif self.standard_deck[j-1].typenum==5:
                    self.standard_deck[j-1].card_name="5"
                    self.standard_deck[j-1].card_value.append(5)
                    self.standard_deck[j-1].card_value.append(5)
                    self.standard_deck[j-1].card_count=1
                elif self.standard_deck[j-1].typenum==6:
                    self.standard_deck[j-1].card_name="6"
                    self.standard_deck[j-1].card_value.append(6)
                    self.standard_deck[j-1].card_value.append(6)
                    self.standard_deck[j-1].card_count=1
                elif self.standard_deck[j-1].typenum==7:
                    self.standard_deck[j-1].card_name="7"
                    self.standard_deck[j-1].card_value.append(7)
                    self.standard_deck[j-1].card_value.append(7)
                    self.standard_deck[j-1].card_count=0
                elif self.standard_deck[j-1].typenum==8:
                    self.standard_deck[j-1].card_name="8"
                    self.standard_deck[j-1].card_value.append(8)
                    self.standard_deck[j-1].card_value.append(8)
                    self.standard_deck[j-1].card_count=0
                elif self.standard_deck[j-1].typenum==9:
                    self.standard_deck[j-1].card_name="9"
                    self.standard_deck[j-1].card_value.append(9)
                    self.standard_deck[j-1].card_value.append(9)
                    self.standard_deck[j-1].card_count=0
                elif self.standard_deck[j-1].typenum==10:
                    self.standard_deck[j-1].card_name="10"
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_count=-1
                elif self.standard_deck[j-1].typenum==11:
                    self.standard_deck[j-1].card_name="Jack"
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_count=-1
                elif self.standard_deck[j-1].typenum==12:
                    self.standard_deck[j-1].card_name="Queen"
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_count=-1
                elif self.standard_deck[j-1].typenum==13:
                    self.standard_deck[j-1].card_name="King"
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_count=-1     
            elif j<40:
                self.standard_deck[j-1].typenum=j-26
                self.standard_deck[j-1].card_suite="Diamonds"
                if self.standard_deck[j-1].typenum==1:
                    self.standard_deck[j-1].card_name="Ace"
                    self.standard_deck[j-1].card_value.append(1)
                    self.standard_deck[j-1].card_value.append(11)
                    self.standard_deck[j-1].card_count=-1
                elif self.standard_deck[j-1].typenum==2:
                    self.standard_deck[j-1].card_name="2"
                    self.standard_deck[j-1].card_value.append(2)
                    self.standard_deck[j-1].card_value.append(2)
                    self.standard_deck[j-1].card_count=1
                elif self.standard_deck[j-1].typenum==3:
                    self.standard_deck[j-1].card_name="3"
                    self.standard_deck[j-1].card_value.append(3)
                    self.standard_deck[j-1].card_value.append(3)
                    self.standard_deck[j-1].card_count=1
                elif self.standard_deck[j-1].typenum==4:
                    self.standard_deck[j-1].card_name="4"
                    self.standard_deck[j-1].card_value.append(4)
                    self.standard_deck[j-1].card_value.append(4)
                    self.standard_deck[j-1].card_count=1
                elif self.standard_deck[j-1].typenum==5:
                    self.standard_deck[j-1].card_name="5"
                    self.standard_deck[j-1].card_value.append(5)
                    self.standard_deck[j-1].card_value.append(5)
                    self.standard_deck[j-1].card_count=1
                elif self.standard_deck[j-1].typenum==6:
                    self.standard_deck[j-1].card_name="6"
                    self.standard_deck[j-1].card_value.append(6)
                    self.standard_deck[j-1].card_value.append(6)
                    self.standard_deck[j-1].card_count=1
                elif self.standard_deck[j-1].typenum==7:
                    self.standard_deck[j-1].card_name="7"
                    self.standard_deck[j-1].card_value.append(7)
                    self.standard_deck[j-1].card_value.append(7)
                    self.standard_deck[j-1].card_count=0
                elif self.standard_deck[j-1].typenum==8:
                    self.standard_deck[j-1].card_name="8"
                    self.standard_deck[j-1].card_value.append(8)
                    self.standard_deck[j-1].card_value.append(8)
                    self.standard_deck[j-1].card_count=0
                elif self.standard_deck[j-1].typenum==9:
                    self.standard_deck[j-1].card_name="9"
                    self.standard_deck[j-1].card_value.append(9)
                    self.standard_deck[j-1].card_value.append(9)
                    self.standard_deck[j-1].card_count=0
                elif self.standard_deck[j-1].typenum==10:
                    self.standard_deck[j-1].card_name="10"
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_count=-1
                elif self.standard_deck[j-1].typenum==11:
                    self.standard_deck[j-1].card_name="Jack"
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_count=-1
                elif self.standard_deck[j-1].typenum==12:
                    self.standard_deck[j-1].card_name="Queen"
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_count=-1
                elif self.standard_deck[j-1].typenum==13:
                    self.standard_deck[j-1].card_name="King"
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_count=-1
                    
            elif j<53:
                self.standard_deck[j-1].typenum=j-39
                self.standard_deck[j-1].card_suite="Hearts"
                if self.standard_deck[j-1].typenum==1:
                    self.standard_deck[j-1].card_name="Ace"
                    self.standard_deck[j-1].card_value.append(1)
                    self.standard_deck[j-1].card_value.append(11)
                    self.standard_deck[j-1].card_count=-1
                elif self.standard_deck[j-1].typenum==2:
                    self.standard_deck[j-1].card_name="2"
                    self.standard_deck[j-1].card_value.append(2)
                    self.standard_deck[j-1].card_value.append(2)
                    self.standard_deck[j-1].card_count=1
                elif self.standard_deck[j-1].typenum==3:
                    self.standard_deck[j-1].card_name="3"
                    self.standard_deck[j-1].card_value.append(3)
                    self.standard_deck[j-1].card_value.append(3)
                    self.standard_deck[j-1].card_count=1
                elif self.standard_deck[j-1].typenum==4:
                    self.standard_deck[j-1].card_name="4"
                    self.standard_deck[j-1].card_value.append(4)
                    self.standard_deck[j-1].card_value.append(4)
                    self.standard_deck[j-1].card_count=1
                elif self.standard_deck[j-1].typenum==5:
                    self.standard_deck[j-1].card_name="5"
                    self.standard_deck[j-1].card_value.append(5)
                    self.standard_deck[j-1].card_value.append(5)
                    self.standard_deck[j-1].card_count=1
                elif self.standard_deck[j-1].typenum==6:
                    self.standard_deck[j-1].card_name="6"
                    self.standard_deck[j-1].card_value.append(6)
                    self.standard_deck[j-1].card_value.append(6)
                    self.standard_deck[j-1].card_count=1
                elif self.standard_deck[j-1].typenum==7:
                    self.standard_deck[j-1].card_name="7"
                    self.standard_deck[j-1].card_value.append(7)
                    self.standard_deck[j-1].card_value.append(7)
                    self.standard_deck[j-1].card_count=0
                elif self.standard_deck[j-1].typenum==8:
                    self.standard_deck[j-1].card_name="8"
                    self.standard_deck[j-1].card_value.append(8)
                    self.standard_deck[j-1].card_value.append(8)
                    self.standard_deck[j-1].card_count=0
                elif self.standard_deck[j-1].typenum==9:
                    self.standard_deck[j-1].card_name="9"
                    self.standard_deck[j-1].card_value.append(9)
                    self.standard_deck[j-1].card_value.append(9)
                    self.standard_deck[j-1].card_count=0
                elif self.standard_deck[j-1].typenum==10:
                    self.standard_deck[j-1].card_name="10"
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_count=-1
                elif self.standard_deck[j-1].typenum==11:
                    self.standard_deck[j-1].card_name="Jack"
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_count=-1
                elif self.standard_deck[j-1].typenum==12:
                    self.standard_deck[j-1].card_name="Queen"
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_count=-1
                elif self.standard_deck[j-1].typenum==13:
                    self.standard_deck[j-1].card_name="King"
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_value.append(10)
                    self.standard_deck[j-1].card_count=-1
     
##GameDeck object keeps a collection of card objects in the Available_Cards object. 
class GameDeck:
    
    def __init__(self, num_decks):
        self.Available_Cards=[]
        self.Card_Holder=[] 
        self.Card_List=[]
        for i in range(num_decks):
            self.Card_Holder.append(Deck())
        for j in range(num_decks):
            for k in range(1,53):
                    self.Available_Cards.append(self.Card_Holder[j].standard_deck[k-1])
                    
    def shuffle_game_deck(self):
        random.shuffle(self.Available_Cards)
        
    def see_deck(self):
        for i in range(len(self.Available_Cards)):
            self.Card_List.append(self.Available_Cards[i].typenum)
        print self.Card_List
            
