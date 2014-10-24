from __future__ import division
from CardandDeck import GameDeck
from Player import Player
from Player import Dealer
from Player import COMP_Player
from CardandDeck import card

#This is the human vs dealer interface
#Shuffle_Req is the minimum number of cards that must be in the deck for a game to start
def Game(Shuffle_Req=52):
    Game_Play=True
    while Game_Play:
        print "Do you want to start a game"
        print "1. Yes"
        print "2. No"
        Game_Play_Choice=raw_input("Enter number corresponding to your choice")
        GPC=int(Game_Play_Choice)
        if GPC!=1:
            Game_Play=False
            break
        if GPC==1:
            Deck=GameDeck(4)
            Deck.shuffle_game_deck()
            players=[]
            number_of_players=raw_input("Number of Players")
            NUM_Players=int(number_of_players)
            Game_Number=1
            d=0
            v=0
            while d < NUM_Players*5:
                if d%5==0:
                    v=v+1               
                    
                    h=d+1
                    players.append(Player())
                    players[d].key=v
                    extra=1
                    print "Player %d" %players[d].key
                    d=d+1
                    ##this was coded to allow keeping track of total gains and losses for a given player. Tack can still be kept without the below statments and each player is assumed to stat with zero
##                    Cash_Available=raw_input("Amount of Cash")
##                    Bet=raw_input("Place bet")
        
                
##                    players[d-1].cash=int(Cash_Available)
                    continue
                    ## the next couple lines are used to set up set up places for split hands. Up to four split hands are allowed.
                else:
                    e=d%5
                    
                    players.append(Player())
                    players[d].key=v
                    players[d].playing_status=False
                    
                    players[d].turn_status=False
                    
                    players[d].Hand_number=e
                    
                    d=d+1
                    continue
            GameDealer=Dealer()
        
            
            while len(Deck.Available_Cards)>Shuffle_Req:
                #asks players for they bets
                z=0
                while z<NUM_Players*5:
                    if z%5==0:
                        print "Player %d" %players[z].key
                        Bet=raw_input("Place bet")
                        players[z].bet=int(Bet)
                        z=z+1
                    else:
                        z=z+1
                    
                #establishes game dealers hand
                GameDealer.Get_Cards(Deck)
                
                players.append(GameDealer)
                #deals each player 2 cards
                for i in range(len(players)-1):
                    if players[i].playing_status==True:
                        players[i].Get_Cards(Deck)
                    else:
                        continue
               
                #Here is where players take their turns. Players ability to split and double down are limited to situations when their active hand is of size 2
                # splitting and doubline down are allowed after hands are split only on the turn were the split hand is of size 2
                #Also the system returns your array of hand values.
                #one a play has been made, surrendering is not allowed for that player during a given round
                #Ability to make decisions (split, hit, double down, stand, surrender) are determined the attributtes Split_stats, Hit_status, Double_Down_status, Stand_status, and Surrender
                print "Game starts now"
                for i in range(len(players)-1):
                    while players[i].turn_status==True and players[i].playing_status==True and players[i].Bust_status==False:
                        print "Player %d turn" %players[i].key 
                        print "Hand %d" %(players[i].Hand_number)
                        players[i].Print_Hand()
                        print players[i].hand_value
                        if len(players[i].hand)==2:
                            players[i].Double_Down_status=True
                            players[i].Split_status=True
                        else:
                            players[i].Double_Down_status=False
                            players[i].Split_status=False
                        if players[i].Hit_status==True:
                            print "1. Hit"
                        if players[i].Double_Down_status==True:
                            print "2. Double Down"
                        if players[i].Surrender_status==True:
                            print "3. Surrender"
                        if players[i].Stand_status==True:
                            print "4. Stand"
                        if players[i].Split_status==True:
                            print "5. Split"
                        choice_number=raw_input("Enter choice")
                        choice=int(choice_number)
                        if choice==1 and players[i].Hit_status==True:
                            print players[i].Print_Hand()
                            players[i].Hit(Deck,1)

                               
                        elif choice==2 and players[i].Double_Down_status==True:
                            players[i].Double_Down(Deck,1)

                        elif choice==3 and players[i].Surrender_status==True:
                            players[i].Surrender()

                        elif choice==4 and players[i].Stand_status==True:
                            players[i].Stand()

                        elif choice==5 and players[i].Split_status==True and len(players[i].hand)==2 and players[i].hand[0].card_value==players[i].hand[1].card_value:
                            x=1
                            while(x<5):
                                if players[i+x].playing_status==False and players[i+x].key==players[i].key:
                                    players[i+x].playing_status=True
                                    players[i+x].turn_status=True
                                    players[i+x].hand.append(players[i].hand.pop())
                                    players[i+x].bet=players[i].bet
                                    players[i].Surrender_status=False
                                    players[i+x].Surrender_status=False
                                    
                                    if players[i].hand[0].card_value[0]==players[i].hand[0].card_value[1]:
                                        
                                        players[i].hand_value=[]
                                        players[i+x].hand_value=[]
                                        
                                        players[i].hand_value.append(players[i].hand[0].card_value[0])
                                        players[i+x].hand_value.append(players[i].hand[0].card_value[0])
                                    else:
                                        players[i].hand_value=players[i].hand[0].card_value
                                        players[i+x].hand_value=players[i].hand[0].card_value
                                    
                                    
                                    break

                                else:
                                    
                                    x=x+1
                                    
                                    continue
                                    
                                    
                        else:
                            continue
                    continue
                #Here we establish that the dealer will stand on hard 17, 18, hard 18, and higher and hit on everything else
                Dealer_Hit=True
                while(Dealer_Hit==True):
                    print "Dealer Hand"
                    players[len(players)-1].Print_Hand()
                    if all(soft_17<17 for soft_17 in players[len(players)-1].hand_value) and players[len(players)-1].Best_Value()<=17:
                        players[len(players)-1].Hit(Deck)
                    else:
                        Dealer_Hit=False
                        break
                if all(card_values>21 for card_values in players[i].hand_value):
                            players[i].Bust_status=True
                            
                #Here we establish the rules of winning and loosing. Ties are pushed. Wins with blackjack are returned with 1.5 the bet value. Losses result in losses of the bet value.
                for i in range(len(players)-2):
                    if i%5==0:
                        split_hands=0
                        while split_hands<5:
                            if players[i+split_hands].playing_status==True:
                                if players[i+split_hands].Bust_status==True:
                                    players[i].cash-=players[i+split_hands].bet
                                    players[len(players)-1].cash+=players[i+split_hands].bet
                                    players[i+split_hands].bet=0
                                    print "Player %d lost on hand %d" %(players[i+split_hands].key, players[i+split_hands].Hand_number)
                                    

                                elif players[i+split_hands].Bust_status==False and players[len(players)-1].Bust_status==True:
                                    if players[i+split_hands].Best_Value()==21 and len(players[i+split_hands].hand)==2:
                                        players[i+split_hands].bet=players[i+split_hands].bet*1.5
                                    players[i].cash+=players[i+split_hands].bet
                                    players[len(players)-1].cash+=players[i+split_hands].bet
                                    players[i+split_hands].bet=0
                                    print "Player %d won on hand %d" %(players[i+split_hands].key, players[i+split_hands].Hand_number)
                                elif players[i+split_hands].Bust_status==False and players[len(players)-1].Bust_status==False:
                                    players[i+split_hands].hand_value.sort()
                                    players[len(players)-1].hand_value.sort()
                                    if players[i+split_hands].Best_Value()<players[len(players)-1].Best_Value():
                                        players[i].cash-=players[i+split_hands].bet
                                        players[len(players)-1].cash-=players[i+split_hands].bet
                                        players[i+split_hands].bet=0
                                        print "Player %d lost on hand %d" %(players[i+split_hands].key, players[i+split_hands].Hand_number)
                                    elif players[i+split_hands].Best_Value()>players[len(players)-1].Best_Value():
                                        if players[i+split_hands].Best_Value()==21 and len(players[i+split_hands].hand)==2:
                                            players[i+split_hands].bet=players[i+split_hands].bet*1.5
                                        players[i].cash+=players[i+split_hands].bet
                                        players[len(players)-1].cash+=players[i+split_hands].bet
                                        players[i+split_hands].bet=0
                                        print "Player %d won on hand %d" %(players[i+split_hands].key, players[i+split_hands].Hand_number)
                                    elif players[i+split_hands].Best_Value()==players[len(players)-1].Best_Value():
                                        players[i+split_hands].bet=0
                                        print"Player %d pushed on hand %d" %(players[i+split_hands].key, players[i+split_hands].Hand_number)
                            split_hands=split_hands+1
                    

                    continue
                #shows the players what there total gains/losses are at the end of each round
                for i in range(len(players)-1):
                    if i%5==0:
                        print "Players %d Cash" %players[i].key
                        print players[i].cash
                #gets the players ready for the next round by setting statuses back to default.
                for i in range(len(players)-1):
                    players[i].bet=0
                    players[i].hand=[]
                    players[i].hand_value=[0]
                    players[i].turn_status=True
                    players[i].playing_status=True
                    players[i].Bust_status=False
                    players[i].Hit_status=True
                    players[i].Double_Down_status=True
                    players[i].Surrender_status=True
                    players[i].Stand_status=True
                    if i%5!=0:
                        players[i].playing_status=False
                        players[i].turn_status=False
                players.pop()
                GameDealer.hand=[]
                GameDealer.hand_value=[0]
                Game_Number=Game_Number+1
                
                

                continue
            
#############################################################################
##Simulation function has the same protocal as above but uses the automated player to make decisions where the human players make decisions above
def Simulation(Shuffle_Req=52, num_players=1, num_games=1, decks_used=2):
    Game_Play=0
    win_count=0
    loss_count=0
    games_played=0
    tie_count=0
    winnings=0
    total_waged=0
    total_risk=0
    while Game_Play<num_games:
  
        
        
        Deck=GameDeck(decks_used)
        
        players=[]
        NUM_Players=num_players
        Game_Number=1
        discarded_cards=[]
        Deck.shuffle_game_deck()
        
        while len(Deck.Available_Cards)>Shuffle_Req:
            discard_len=len(discarded_cards)
            number_of_decks=((decks_used*52)-discard_len)/52

            d=0
            v=0
            while d < NUM_Players*5:
                if d%5==0:
                    v=v+1               
                    
                    h=d+1
                    players.append(COMP_Player(0, number_of_decks, 10))
                    players[d].key=v
                    extra=1
                    d=d+1

                    continue

                else:
                    e=d%5
                    
                    players.append(COMP_Player())
                    players[d].key=v
                    players[d].playing_status=False
                    
                    players[d].turn_status=False
                    
                    players[d].Hand_number=e
                    
                    d=d+1
                    continue
            for i in range(len(players)):
                players[i].Make_Bet_Dec(discarded_cards)
                  
            players[0].seen_cards=[]
            
                
                       

                      
            GameDealer=Dealer()
            GameDealer.Get_Cards(Deck)
            players.append(GameDealer)
            
            
            for i in range(len(players)-1):
                if players[i].playing_status==True:
                    players[i].Get_Cards(Deck)
                else:
                    continue
            face_down_card=GameDealer.hand[0]
            unknown_cards=Deck
            unknown_cards.Available_Cards.append(face_down_card)
    
            for i in range(len(players)-1):
                while players[i].turn_status==True and players[i].playing_status==True and players[i].Bust_status==False:
##options list keeps track of what the automated player can do
                    options=[]
                    if len(players[i].hand)==2:
                        players[i].Double_Down_status=True
                        players[i].Split_status=True
                    else:
                        players[i].Double_Down_status=False
                        players[i].Split_status=False
            
                    if players[i].Hit_status==True:
                        options.append(1)
                    if players[i].Double_Down_status==True:
                        options.append(2)
                    if players[i].Surrender_status==True:
                        options.append(3)
                    if players[i].Stand_status==True:
                        options.append(4)
                    if players[i].Split_status==True:
                        options.append(5)
                        ## here is where the atuomated player makes the decision. Look at Player library for method
                    choice=players[i].Play_Hand(unknown_cards, face_down_card, options)
                    if choice==1 and players[i].Hit_status==True:
                        players[i].Hit(Deck,0)
     
                    elif choice==2 and players[i].Double_Down_status==True:
                        players[i].Double_Down(Deck,0)
                    elif choice==3 and players[i].Surrender_status==True:
                        players[i].Surrender()

                    elif choice==4 and players[i].Stand_status==True:
                        players[i].Stand()
                    elif choice==5 and players[i].Split_status==True and len(players[i].hand)==2 and players[i].hand[0].card_value==players[i].hand[1].card_value:
                        x=1
                        while(x<5):
                            if players[i+x].playing_status==False and players[i+x].key==players[i].key:
                                players[i+x].playing_status=True
                                players[i+x].turn_status=True
                                players[i+x].hand.append(players[i].hand.pop())
                                players[i+x].bet=players[i].bet
                                players[i].Surrender_status=False
                                players[i+x].Surrender_status=False
                            
                                
                                if players[i].hand[0].card_value[0]==players[i].hand[0].card_value[1]:
                                        
                                    players[i].hand_value=[]
                                    players[i+x].hand_value=[]
                                    
                                    players[i].hand_value.append(players[i].hand[0].card_value[0])
                                    players[i+x].hand_value.append(players[i].hand[0].card_value[0])
                                else:
                                    players[i].hand_value=players[i].hand[0].card_value
                                    players[i+x].hand_value=players[i].hand[0].card_value
                                break

                            else:
                                
                                x=x+1
                                
                                continue
                                
                                
                    else:
                        continue
                continue
            
            Dealer_Hit=True
            while(Dealer_Hit==True):
##                print "Dealers Hand"
##                players[len(players)-1].Print_Hand()
                if all(soft_17<17 for soft_17 in players[len(players)-1].hand_value) and players[len(players)-1].Best_Value()<=17:
                    players[len(players)-1].Hit(Deck)
                else:
                    Dealer_Hit=False
                    break
            for g in players[0].seen_cards:
                discarded_cards.append(g)
            for g in players[len(players)-1].hand:
                discarded_cards.append(g)
                
            players[len(players)-1].seen_cards=[]
            
            if all(card_values>21 for card_values in players[i].hand_value):
                players[i].Bust_status=True

            for i in range(len(players)-1):
                if i%5==0:
                    split_hands=0
                    while split_hands<5:
                        if players[i+split_hands].playing_status==True:
                            if players[i+split_hands].Bust_status==True:
                                players[i].cash-=players[i+split_hands].bet
                                winnings=winnings-players[i+split_hands].bet
                                total_waged=total_waged+players[i+split_hands].bet
                                total_risk=total_risk+players[i+split_hands].bet
                                players[len(players)-1].cash+=players[i+split_hands].bet
                                players[i+split_hands].bet=0
                                games_played=games_played+1
                                loss_count=loss_count+1
                                
##                                    print "Player %d lost on hand %d" %(players[i+split_hands].key, players[i+split_hands].Hand_number)
                                

                            elif players[i+split_hands].Bust_status==False and players[len(players)-1].Bust_status==True:
                                if players[i+split_hands].Best_Value()==21 and len(players[i+split_hands].hand)==2:
                                    players[i+split_hands].bet=players[i+split_hands].bet*1.5
                                players[i].cash+=players[i+split_hands].bet
                                players[len(players)-1].cash+=players[i+split_hands].bet
                                winnings=players[i+split_hands].bet+winnings
                                total_waged=total_waged+players[i+split_hands].bet
                                total_risk=total_risk+players[i+split_hands].bet
                                players[i+split_hands].bet=0
                                win_count=win_count+1
                                games_played=games_played+1
##                                    print "Player %d won on hand %d" %(players[i+split_hands].key, players[i+split_hands].Hand_number)
                            elif players[i+split_hands].Bust_status==False and players[len(players)-1].Bust_status==False:
                                players[i+split_hands].hand_value.sort()
                                players[len(players)-1].hand_value.sort()
                                if players[i+split_hands].Best_Value()<players[len(players)-1].Best_Value():
                                    players[i].cash-=players[i+split_hands].bet
                                    players[len(players)-1].cash-=players[i+split_hands].bet
                                    winnings=winnings-players[i+split_hands].bet
                                    total_waged=total_waged+players[i+split_hands].bet
                                    total_risk=total_risk+players[i+split_hands].bet
                                    players[i+split_hands].bet=0
                                    loss_count=loss_count+1
                                    games_played=games_played+1
##                                        print "Player %d lost on hand %d" %(players[i+split_hands].key, players[i+split_hands].Hand_number)
                                elif players[i+split_hands].Best_Value()>players[len(players)-1].Best_Value():
                                    if players[i+split_hands].Best_Value()==21 and len(players[i+split_hands].hand)==2:
                                        players[i+split_hands].bet=players[i+split_hands].bet*1.5
                                    players[i].cash+=players[i+split_hands].bet
                                    players[len(players)-1].cash+=players[i+split_hands].bet
                                    winnings=winnings+players[i+split_hands].bet
                                    total_waged=total_waged+players[i+split_hands].bet
                                    total_risk=total_risk+players[i+split_hands].bet
                                    
                                    players[i+split_hands].bet=0
                                    win_count=win_count+1
                                    games_played=games_played+1
##                                        print "Player %d won on hand %d" %(players[i+split_hands].key, players[i+split_hands].Hand_number)
                                elif players[i+split_hands].Best_Value()==players[len(players)-1].Best_Value():
                                    total_waged=total_waged+players[i+split_hands].bet
                                    
                                    players[i+split_hands].bet=0
                                    tie_count=tie_count+1
                                    games_played=games_played+1
##                                        print"Player %d pushed on hand %d" %(players[i+split_hands].key, players[i+split_hands].Hand_number)
                        split_hands=split_hands+1


 
                
                
                
                continue
            
            Game_Number=Game_Number+1
            
            players=[]
            
            
            

            continue
    
        Game_Play=Game_Play+1
        ##Hands played is higher than the number entered in the protocal (Number of simulated games) because simulated games result in muliple hands.
        ##Here a game as defined as however long it takes to get down to a 52 card deck. So there are many hands played for each game. Also whenever a split occurs
        ## this increases the number of hands played by 1. 
    print "Hands played %d" %games_played
    print "Wins"
    print win_count
    print "Ties"
    print tie_count
    print "Losses"
    print loss_count
    print "Win Rate "
    print (win_count/games_played)
    print "Loss Rate "
    print (loss_count/games_played)
    print "Winnings"
    print winnings
    ##total waged is the total amount put up. total at risk is does not include hands that were pushed. 
    print "Total Waged"
    print total_waged
    print "Total at risk"
    print total_risk
    print "Return for Waged"
    print winnings/total_waged
    print "Return for Risk"
    print winnings/total_risk
 #################################################       
        
def Protocal():
    print "Play Game or run simulation"
    print "1. Game"
    print "2. Simulation"
    choice=raw_input()
    if int(choice)==1:
        Game()
    else:
        a=int(raw_input("Number of Games"))
        b=int(raw_input("Number of Decks. Must be greater 1"))
        if b>2:
            Simulation(52, 1, a, b)
        else:
            Simulation(52, 1, a, 2)

Protocal()

 
        
                        
                
                        
                   
        
    
