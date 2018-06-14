#juliagolder
#5/23/18
#Yahtzee.py

from random import randint
 

def printRoll(dice): #prints out list of dice
    print(dice)
    

def printCard(scoreL): #prints out scorecard
    print('1: Aces -', scoreL[0])
    print('2: Twos -', scoreL[1])
    print('3: Threes -', scoreL[2])
    print('4: Fours -', scoreL[3])
    print('5: Fives -', scoreL[4])
    print('6: Sixes -', scoreL[5])
    print('7: Three of a Kind -', scoreL[6])
    print('8: Four of a Kind', scoreL[7])
    print('9: Full House -', scoreL[8])
    print('10: Small Straight -', scoreL[9])
    print('11: Large Straight -', scoreL[10])
    print('12: YAHTZEE! -', scoreL[11])



def enterScore(num, dice, scoreL): #tallies up score of the roll
    score = 0
    if num == 1:
        score = L.count(1)
    if num == 2:
        score = L.count(2)*2
    if num == 3:
        score = L.count(3)*3
    if num == 4:
        score = L.count(4)*4
    if num == 5:
        score = L.count(5)*5
    if num == 6:
        score = L.count(6)*6
    if num == 7:
        if is3ofakind(L):
            score = sum(L)
        else:
            score = 0
    if num == 8:
        if is4ofakind(L):
            score = sum(L)
        else:
            score = 0
    if num == 9:
        if isfullhouse(L):
            score = sum(L)
        else:
            score = 0
    if num == 10:
        if isSmallStraight(L):
            score = 30
        else:
            score = 0
    if num == 11:
        if isLargeStraight(L):
            score = 40
        else:
            score = 0
    if num == 12:
        if isYahtzee(L):
            score = 50
        else:
            score = 0
    scoreL[num-1] = score

def is3ofakind(L): #function for determining rolls with three of a kind
    for i in range(1,7):
        if L.count(i) >= 3:
            return True
    return False
    
def is4ofakind(L): #function for determining rolls with four of a kind
    for i in range(1,7):
        if L.count(i) >= 4:
            return True
    return False

"""
def isfullhouse(L): #function for determining rolls with a full house
    L.sort(i)
    if L[0] == L[1] and L[0] == L[2] and L[3] == L[4]:
        return True
    if L[0] == L[1] and L[2] == L[3] and L[2] == L[4]: 
        return True
    return False
"""
 
def isSmallStraight(L): #function for determining rolls with a small straight
    for i in L:
        if (1 in L and 2 in L and 3  in L and 4 in L) or (2 in L and 3 in L and 4  in L and 5 in L or 3 in L and 4 in L and 5  in L and 6 in L):
            return True
    return False


def isLargeStraight(L): #function for determining rolls with a large straight
    for i in L:
        if (1 in L and 2 in L and 3  in L and 4 in L and 5 in L) or (2 in L and 3 in L and 4  in L and 5 in L and 6 in L):
            return True
    return False
    
def isYahtzee(L): #function for determining rolls with a Yahtzee
    for i in range(1,7):
        if L.count(i) == 6:
            return True
    return False

def rollDice(L,pick): #function that allows the user to pick which die they want to reroll
    for i in range(5):
        if i in pick:
            L[i] = (randint(1,6))

if __name__ == '__main__': #sets up and runs the game


    L = [0,0,0,0,0] # a blank list with placeholders for dice
    
    scoreL = [' ']*12 #list for score card
    for i in range(12):    
        #allows the user to roll and reroll specific dice
        rollDice(L,[0,1,2,3,4]) #gives numbers to each die
        printRoll(L) 
        again = input('Do you want to roll again?')
        if again == 'y' or again == 'yes':
            which = input('Which dice do you want to roll?').split(' ')
            toRoll = []
            for die in which:
                toRoll.append(int(die)-1)
            rollDice(L,toRoll)
            printRoll(L)
            again = input('Do you want to roll again?')
            if again == 'y' or again == 'yes':
                which = input('Which dice do you want to roll?').split(' ')
                toRoll = []
                for die in which:
                    toRoll.append(int(die)-1)
                rollDice(L,toRoll)
                printRoll(L)

        #allows user to pick catagory and display score card
        printCard(scoreL)
        chose = int(input('What number do you want to choose?'))
        enterScore(chose,L,scoreL)
        printCard(scoreL)
    print('Your final score is', sum(scoreL), '!')