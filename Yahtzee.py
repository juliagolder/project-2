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
        
    

"""    
def printCard:
    
"""

if __name__ == '__main__':


    L = []
    
    for i in range(5):
        L.append(randint(1,6))
    
    printRoll(L)
