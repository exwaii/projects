############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
     

from random import randint
from math import ceil
print(logo)
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal():
    return cards[randint(1,len(cards)-1)]
def score(hand):
    points=0
    for card in hand:
        points+=card
    return points

while True:
    phand=[deal() for i in range(1,3)]
    dhand=[deal() for i in range(1,3)]
    gameend=False
    pscore=score(phand)
    dscore=score(dhand)
    if dscore>21:
        dhand[0]=1
        dscore=score(dhand)
    if pscore>21:
        phand[0]=1
        pscore=score(phand)
    print(f"dealer hand is {dhand[:-1]+['*']}")
    print(f"your hand is {phand}. your score is {pscore}")
    while True:
        hit=input("hit? y/n ")
        if hit!="y":
            break
        phand.append(deal())
        pscore=score(phand)
        if pscore>21:
            if 11 not in phand:
                print(f"your hand is {phand}. your score is {pscore}")
                print("bust. you lose")
                gameend=True
                break
            elif phand.count(11)*10<(pscore-21):
                for i in range(len(phand)):
                    if phand[i]==11:
                        phand[i]=1
                print(f"your hand is {phand}. your score is {pscore}")
                print("you bust. you lose")
                gameend=True
                break
            else:
                for i in range(1,ceil((pscore-21)/10)):
                    phand[phand.index(11)]=1
                    pscore=score(phand)
        print(f"your hand is {phand}. your score is {pscore}")
        if pscore==21:
            break
    if not gameend:
        while dscore<17:
            dhand.append(deal())
            dscore=score(dhand)
            if dscore>21:
                if 11 not in dhand:
                    print(f"dealers hand is {dhand} his score is {dscore}")
                    print("you win")
                    gameend=True
                elif dhand.count(11)*10<(dscore-21):
                    for i in range(len(phand)):
                        if dhand[i]==11:
                            dhand[i]=1
                        dscore=score(dhand)
                    print(f"dealers hand is {dhand} his score is {dscore}")
                    print("you win")
                    gameend=True
                else:
                    for i in range(1,ceil((dscore-21)/10)):
                        dhand[dhand.index(11)]=1
                        dscore=score(dhand)
    if not gameend:
        print(f"dealers hand is {dhand} his score is {dscore}")
        if dscore>pscore:
            print("you lose")
        elif dscore==pscore:
            print("draw")
        else:
            print("you win")
    if input("continue?y/n " )=="n":
        break
    

                    
    

        


