#juliagolder
#5/23/18
#Yahtzee.py

from random import randint
 

def printRoll(dice):
    print(dice)
    ask1 = input('roll die 1 again?')
    if ask1 == 'yes' or ask1 == 'y':
        cha1 = randint(1,6)
        L[0]=cha1
        print(L)
    ask2 = input('roll die 2 again?')
    if ask2 == 'yes' or ask2 == 'y':
        cha2 = randint(1,6)
        L[1]=cha2
        print(L)
    ask3 = input('roll die 3 again?')
    if ask3 == 'yes' or ask3 == 'y':
        cha3 = randint(1,6)
        L[2]=cha3
        print(L)
    ask4 = input('roll die 4 again?')
    if ask4 == 'yes' or ask4 == 'y':
        cha4 = randint(1,6)
        L[3]=cha4
        print(L)
    ask5 = input('roll die 5 again?')
    if ask5 == 'yes' or ask5 == 'y':
        cha5 = randint(1,6)
        L[4]=cha5
        print(L)
        
    

def printCard():
    print('1: Aces')
    print('2: Twos')
    print('Threes')
    print('Fours')
    print('Fives')
    print('Sixes')
    print('Three of a Kind')
    print('Four of a Kind')
    print('Full House')
    print('Small Straight')
    print('Large Straight')
    print('YAHTZEE!')

def enterScore(num, dice):
    if num == 1:
        L.count('1')
        

def is3ofakind(L):
    for i in range(1,7):
        if L.count(i) >= 3:
            return True
    return False
    
def is4ofakind(L):
    for i in range(1,7):
        if L.count(i) >= 4:
            return True
    return False

""" 
def isfullhouse(L):
    for i in range(1,7)
        if L.count(i) == 3 and L.count(i) == 2:
            return True
    return False
    
def isSmallStraight(L):
    for i in L:
        if 1 in line and 2 in line and 3  in line and 4 in line and 5 in line:
            return True
    return False

def isLargeStraight(L):
    for i in L:
        if 2 in line and 2 in line and 4  in line and 5 in line and 6 in line:
            return True
    return False
    
def isYahtzee(L):
    for i in range(1,7):
        if L.count(i) == 6:
            return True
    return False
"""

if __name__ == '__main__':


    L = []
    
    for i in range(5):
        L.append(randint(1,6))
    
    printRoll(L)
    printCard()
    chose = int(input('What number do you want to choose?'))
    is3ofakind(L)
    is4ofakind(L)
    enterScore(chose,L)
    """
    isfullhouse(L)
    isSmallStraight(L)
    isLargeStraight(L)

    isYahtzee(L)
    """