from __future__ import division
from CardandDeck import card
from CardandDeck import GameDeck
import random
###################
#This file contains the Player class and all of its derived classes (COMP_Player and Dealer)
###################



class Player:
    seen_cards=[]
    seen_dealer_card=[]
    unseen_cards=[]
    #For the computer player it is ncessary to keep track of seen_cards for the betting strategy to have any effect
    #_status attribtes are used to make decisiosn as to whether or not a player can do certain things during the game
    def __init__(self):
        self.key=0
        self.hand=[]
        self.cash=0
        self.bet=0
        self.hand_value=[0]
        self.potential_value=[]
        self.playing_status=True
        self.turn_status=True
        self.Hit_status=True
        self.Double_Down_status=True
        self.Surrender_status=True
        self.Split_status=True
        self.Stand_status=True
        self.Hand_number=0
        self.Bust_status=False
        self.human_status=True
 #Not Used       
    def _Wager_(self, offer):
        self.bet=offer
        self.cash-=offer
 #Gets cards in the dealing part of the game       
    def Get_Cards(self, Deck):
        self.Hit(Deck)
        self.Hit(Deck)
        
 #Gets a card when the player wants to hit                  
    def Hit(self, Deck, show_card=0):
            
            x=len(self.hand_value)
            self.hand.append(Deck.Available_Cards.pop())
            if show_card==1:
                print self.hand[len(self.hand)-1].card_name
            for i in range(x):
                if self.hand[len(self.hand)-1].card_value[1]==self.hand[len(self.hand)-1].card_value[0]:
                    self.hand_value[i]+=self.hand[len(self.hand)-1].card_value[0]

                elif self.hand[len(self.hand)-1].card_value[1]!=self.hand[len(self.hand)-1].card_value[0]:
                    self.hand_value.append(self.hand[len(self.hand)-1].card_value[1]+self.hand_value[i])
                    self.hand_value[i]+=self.hand[len(self.hand)-1].card_value[0]
            self.seen_cards.append(self.hand[len(self.hand)-1])
            if len(self.hand)==3:
                
                self.Surrender_status=False
            if all(card_values>21 for card_values in self.hand_value):
                self.Bust_status=True
            
            return 0
#gets a card when the player wants to hit and doubles the bet
    def Double_Down(self, Deck, show_card=0):
        x=len(self.hand_value)
        self.hand.append(Deck.Available_Cards.pop())
        self.bet=self.bet*2
        if show_card==1:
                print self.hand[len(self.hand)-1].card_name
        for i in range(x):
                if self.hand[len(self.hand)-1].card_value[1]==self.hand[len(self.hand)-1].card_value[0]:
                    self.hand_value[i]+=self.hand[len(self.hand)-1].card_value[0]

                elif self.hand[len(self.hand)-1].card_value[1]!=self.hand[len(self.hand)-1].card_value[0]:
                     self.hand_value.append(self.hand[len(self.hand)-1].card_value[1]+self.hand_value[i])
                     self.hand_value[i]+=self.hand[len(self.hand)-1].card_value[0]
        self.seen_cards.append(self.hand[len(self.hand)-1])
        self.turn_status=False
        if all(card_values>21 for card_values in self.hand_value):
            self.Bust_status=True
        return 1
#ends players turn
    def Stand(self):
        self.bet=self.bet
        self.turn_status=False
        
        return 1
 #returns the players optimal value (highest value not greater than 21)   
    def Best_Value(self):
        value=0
        for i in range(len(self.hand_value)):
            if self.hand_value[i]>value and self.hand_value[i]<=21:
                value=self.hand_value[i]
        return value
#ends players turn and participation in a hand.Gives up half of the bet
    def Surrender(self):
        self.cash-=self.bet/2
        self.turn_status=False
        self.bet=0
        return 2
    def Split(self):
        return 3
    def Print_Hand(self):
        for i in range(len(self.hand)):
            print self.hand[i].card_name
       
class Dealer(Player):
    def __init__(self):
        Player.__init__(self)
        Player.key=-1
            
 #dealer gets a card      
    def Hit(self, Deck):
            x=len(self.hand_value)
            self.hand.append(Deck.Available_Cards.pop())
            for i in range(x):
                if self.hand[len(self.hand)-1].card_value[1]==self.hand[len(self.hand)-1].card_value[0]:
                    self.hand_value[i]+=self.hand[len(self.hand)-1].card_value[0]

                elif self.hand[len(self.hand)-1].card_value[1]!=self.hand[len(self.hand)-1].card_value[0]:
                    self.hand_value.append(self.hand[len(self.hand)-1].card_value[1]+self.hand_value[i])
                    self.hand_value[i]+=self.hand[len(self.hand)-1].card_value[0]
            if len(self.hand)>=2:
                self.seen_cards.append(self.hand[x-1])
                self.seen_dealer_card.append(self.hand[x-1])
            return 0

 #       
class COMP_Player(Player):
    def __init__(self, comp_key=0, n_d=1, m_b=1):
        Player.__init__(self)
        self.human_status=False
        self.key=comp_key
        self.min_bet=m_b
        self.number_decks=n_d
       #uses card count to make betting decision 
    def Make_Bet_Dec(self, cards_info):
        count=0
        for i in range(len(cards_info)):
            count=count+cards_info[i].card_count

        
        true_count=count/self.number_decks
        unit_bet=((true_count-1)/.5)+1

        if unit_bet<0:
            unit_bet=1
        elif unit_bet>7:
            unit_bet=unit_bet*10
        self.bet=self.min_bet*unit_bet

        return self.bet
    #calculates an array of expected values for the next card. There is a different expected value for each ace still in the deck.
    #for n aces in the deck there are 2exp(n) expected values in the array including duplicates
    def Exp_Hit_Value(self,Deck):
        Deck.shuffle_game_deck()
        sum_values=[0]
        i=0
        while i<len(Deck.Available_Cards):
            
            if Deck.Available_Cards[i].card_value[0]==Deck.Available_Cards[i].card_value[1]:
                
                k=0
                z=len(sum_values)
                while k<z:
                    sum_values[k]=sum_values[k]+Deck.Available_Cards[i].card_value[0]
                    k=k+1
            else:
                j=0
                v=len(sum_values)
                while j<v:
                    holder=sum_values[j]
                    sum_values[j]=sum_values[j]+Deck.Available_Cards[i].card_value[0]
                    sum_values.append(holder+Deck.Available_Cards[i].card_value[1])
                    j=j+1
            i=i+1
        

        Exp_Val=[]
        for i in range(len(sum_values)):
            Exp_Val.append(sum_values[i]/len(Deck.Available_Cards))
        return Exp_Val
    #calculates the array of expected values for the next n cards where n is rand_pick. Uses random m random samples with replacemet
    #where m is confidence. 
    def Cond_Exp_Hit_Value(self, Deck, rand_pick=1, confidence=10):
        
        New_stop=0
        Cards=Deck
        Cards.shuffle_game_deck()
        cond_sum=0
        exp_val_sum=[]
        exp_val_matrix=[]
        exp_matrix_len=[]
        divisors=[]
        max_len_matrix=0
        con_exp_vals=[]
        if rand_pick==1:
            con_exp_vals=self.Exp_Hit_Value(Cards)
            return con_exp_vals

        

            
        else:
            i=0
            while i<confidence:
                
                temp=random.sample(Cards.Available_Cards, rand_pick%len(Cards.Available_Cards))
                tempdeck=GameDeck(0)
                exp_val_matrix.append([0])
                
                for b in range(len(temp)):
                    tempdeck.Available_Cards.append(temp[b])
                for e in range(len(tempdeck.Available_Cards)):
                    if tempdeck.Available_Cards[e].card_value[0]==tempdeck.Available_Cards[e].card_value[1]:
                        k=0
                        z=len(exp_val_matrix[i])
                        while k<z:

                            exp_val_matrix[i][k]=exp_val_matrix[i][k]+tempdeck.Available_Cards[e].card_value[0]
                            k=k+1
                    else:
                        k=0
                        z=len(exp_val_matrix[i])
                        while k<z:
                            holder=exp_val_matrix[i][k]
                            exp_val_matrix[i][k]=exp_val_matrix[i][k]+tempdeck.Available_Cards[e].card_value[0]
                            exp_val_matrix[i].append(holder+tempdeck.Available_Cards[e].card_value[1])
                            k=k+1
                i=i+1
                        
                        
            get_len=0                       
            while get_len<len(exp_val_matrix):
                exp_matrix_len.append(len(exp_val_matrix[get_len]))
                if len(exp_val_matrix[get_len])>max_len_matrix:
                    max_len_matrix=len(exp_val_matrix[get_len])
                get_len=get_len+1
            
            for h in range(max_len_matrix):
                exp_val_sum.append(0)
                divisors.append(0)
            t=0
            while t<max_len_matrix:
                for g in range(len(exp_val_matrix)):
                    if exp_matrix_len[g]>t:
                        exp_val_sum[t]=exp_val_sum[t]+exp_val_matrix[g][t]
 
                        y=exp_val_matrix[g][t]
                        divisors[t]=divisors[t]+1
                    else:
                        continue
                t=t+1
            for z in range(len(exp_val_sum)):
                con_exp_vals.append(exp_val_sum[z]/divisors[z])
            return con_exp_vals
                                      
            
            
        ##COMP_Player looks at the expected value of dealers hand. Looks at the n-hit expected value of a single hand of a split hand and splits if
        #the expected value is higher than the dealers and less than or equal to 21. It then checks if the 1-hit expected value of the current hand is less than or equal to
        ##21. If the one hit expected value is higher than the dealers expected value COMP_Playe doubles down. If its 1 hit expected value is less than the dealers expected value
        ## and less than or equal to 21 COMP_Player hits. In all other situations the dealer stands
    def Play_Hand(self, unkown_cards, dealer_card,options, print_status=0):
        exp_value_dealer=dealer_card.card_value
        dealer_next_card=[]
        player_next_card =[0]
        count=1
        countB=1
        countSp=0
        countH=0
        opt_deal_val=False
        opt_play_val=False
        high_dealer_val=0
        opt_split_val=False
        fear_bust=False
        Dec =0
        confidence=40
        ##Gets dealers expected value using random sampling.
        while opt_deal_val==False:
            
            if all(values<17 for values in dealer_next_card) and high_dealer_val<=17 :
                dealer_next_card=self.Cond_Exp_Hit_Value(unkown_cards, count, confidence)
                dealer_next_card.sort()
                
                if dealer_card.card_value[0]==dealer_card.card_value[1]:
                    for i in range(len(dealer_next_card)):
                        dealer_next_card[i]=dealer_card.card_value[0]+dealer_next_card[i]
                else:
                    temp_next_card=dealer_next_card
                    for i in range(len(dealer_next_card)):
                        dealer_next_card[i]=dealer_card.card_value[0]+dealer_next_card[i]
                    for j in range(len(dealer_next_card)):
                        check_in=dealer_card.card_value[1]+temp_next_card[j]
                        if check_in not in dealer_next_card:
                            dealer_next_card.append(dealer_card.card_value[1]+temp_next_card[j])
                 #Gets the optimal value from the dealers array of expected value
                for i in range(len(dealer_next_card)):
                    if dealer_next_card[i]>high_dealer_val and dealer_next_card[i]<=21:
                        high_dealer_val=dealer_next_card[i]
                count=count+1
            else:
                opt_deal_val=True
        dealer_next_card.sort()
       
     
                
        #examines splitting possibilities 
        if len(self.hand)==2:
            if self.hand[0].card_value==self.hand[1].card_value:
                if self.hand[0].card_value[0]!=10 and self.hand[0].card_value[0]!=5:
                    
                    while opt_split_val==False:
                        half_hand=len(self.hand_value)//2
                        single_card_val=self.hand[0].card_value
                        
                        if all(values<=high_dealer_val for values in player_next_card) and any(values<=21 for values in player_next_card):
                            countSp=countSp+1
                            player_next_card=self.Cond_Exp_Hit_Value(unkown_cards, countSp, confidence)
                            player_next_card.sort()
                            temp=player_next_card
                            for i in range(len(single_card_val)):
                                if i==0:
                                    for j in range(len(player_next_card)):
                                        check_in=player_next_card[j]+single_card_val[i]
                                        if check_in not in player_next_card:
                                            player_next_card[j]=temp[j]+single_card_val[i]
                    
                                else:
                                    for j in range(len(player_next_card)):
                                        check_in=temp[j]+single_card_val[i]
                                        if check_in not in player_next_card:
                                            player_next_card.append(temp[j]+single_card_val[i])
                            
                            
                        else:
                           
                
                            opt_split_val=True
                            single_card_val=player_next_card
                            for j in range(len(single_card_val)):
               
                                if single_card_val[j]>high_dealer_val and single_card_val[j]<=21:
                                    if 5 in options:
                                        if print_status==1:
                                            print "SPLIT"
                                        Dec=5
                                        return Dec
                        
        #examines hitting possibilities and doubleing down possibilties
        player_next_card=self.hand_value
        while opt_play_val==False:
            
            if (all(values<high_dealer_val for values in player_next_card) or high_dealer_val==0) and any(values<=21 for values in player_next_card):
                countH=countH+1
                player_next_card=self.Cond_Exp_Hit_Value(unkown_cards, countH, confidence)
                player_next_card.sort()
                temp=player_next_card
                for i in range(len(self.hand_value)):
                    if i==0:
                        for j in range(len(player_next_card)):
                            player_next_card[j]=player_next_card[j]+self.hand_value[i]
                    else:
                        for j in range(len(player_next_card)):
                            player_next_card.append(temp[j]+self.hand_value[i])
                if countH==1:
                    if any(values<=21 for values in player_next_card):
                        if 1 in options:
                            Dec=1
                    
                countB=countB+1
            
                               
            else:
                opt_play_val=True
## Using expected value strategy to decide when to double down is resulting in a negative return. Elminating this section results in an positive
##expected return on average. This section needs to be refined.
                
##                if countH==1 and any(values<=21 for values in player_next_card):
##                    if 2 in options:
##                        if print_status==1:
##                            print "DOUBLE DOWN"
##                        Dec=2
                if Dec!=0:
                    if Dec==1:
                        if print_status==1:
                            print "HIT"
                    return Dec

       
                        
                   
        Dec=4
        if print_status==1:
            print "STAND"
        return Dec
            
            
        
        
        
        
    
                
        

                    
                
        
        
        
        
        
        


##Deck=GameDeck(1)
##player=COMP_Player(1)
##player.Exp_Hit_Value(Deck)
##x=player.Cond_Exp_Hit_Value(Deck, 1, 50)
##print x
        
        
        
    
        
    

    
        
        
        
        
        


    
