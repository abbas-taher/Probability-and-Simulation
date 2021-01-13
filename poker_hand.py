#!/usr/bin/python3
#__author__ = "Abbas Taher"
#__version__ = "0.1"
#__date__="2021.01.10"


"""  Illustrative examples on how to use Flek Machine to do Probability computations
     Basically given a full deck of 52 cards. 
     
     If we are drawing a random sample of 5 cards from the deck (One Pocker hand)
     
     - What is the chance that 4 of the cards are of one kind?
     - What is the chance that we have 3 of one kind and 2 of another (Full House)?
     
     https://en.wikipedia.org/wiki/Poker_probability
      
     In a 52 card game, we have 2,598,960 possible hands. Out of these possibilities there are 
     624 four of a kind hands and 3744 full house hands. Thus, the true probabilities look like this:
      
      Hand	           Possible Hands              Probability
     Four of a Kind	        624                624 /2,598,960  = 0.000240096
     Full House             3744               3744/2,598,960  = 0.00144058
"""

from random import sample
from collections import defaultdict 

NAMES = ['Spade','Club', 'Heart', 'Diamond']
names = ['S','C','H','D']
ranks = ['K','Q','J', '1','2','3','4','5','6','7','8','9','10']
Full_Deck = [ k+c for k in names for c in ranks] 
 
def Generate_Hands(num_hands = 3):    
    """ generate a set of 5-card hands ['CJ','SJ','D3','DK','H9']"""
    for i in range (num_hands):
        hand = sample(Full_Deck, 5)  # generate random hand
        yield (hand)
        
def check(hand):
    groups  = defaultdict(int)
    for card in hand:    
        groups[card[1:]] += 1
    
    if len(groups) == 2:
        if max(groups.values()) == 4 :  # four-of-akind
            return (1,0)
        else:   
            return (0,1)    # max=3 and min=2 -> full house
    return (0,0)   # all other cases
    
def main():
    print (Full_Deck)
    
    four_kind = 0
    full_house =0
    iterations = 300_000
    
    for hand in Generate_Hands(iterations):
        four, full = check (hand)
        four_kind += four
        full_house += full
    
    print ("Probability four of a kind:", four_kind/iterations)  
    print ("Probability full house:", full_house/iterations)
    
    
if __name__ == "__main__":
    main()
     
