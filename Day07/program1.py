#! /usr/bin/env python3
import sys
from functools import cmp_to_key

CARDS = {
        'A':13,
        'K':12,
        'Q':11,
#        'J':10,
        'T':9,
        '9':8,
        '8':7,
        '7':6,
        '6':5,
        '5':4,
        '4':3,
        '3':2,
        '2':1,
        'J':0
        }

def readCards():
    Hands = []
    while line := sys.stdin.readline():
        Hands.append(line.split())

    return Hands

def countHand(hand):
    count = {}
    for c in hand:
        count[c] = count.get(c,0) + 1
    return count

def getType(count):
 
    numJ = count.get('J',0)
    NoJ  = count.copy()
    if 'J' in count:
        NoJ.pop('J')

    NoJ = list(NoJ.values())
    c = list(count.values())  

    # 5 of a kind
    if 5 in c or (4 in c and numJ == 1) or (3 in c and numJ == 2) or (2 in c and numJ == 3) or (1 in c and numJ == 4):
        return 7

    # 4 of a kind
    elif 4 in c or (3 in c and numJ == 1) or (2 in NoJ and numJ == 2) or (1 in c and numJ == 3):
        return 6

    # full house
    elif (3 in c and 2 in c) or (c.count(2) == 2 and numJ == 1) or (NoJ.count(2) == 1 and numJ == 2):
        return 5

    # 3 of a kind
    elif 3 in c or (2 in c and numJ == 1) or (1 in c and numJ == 2):
        return 4

    # 2 pair
    elif (2 in c and c.count(2) == 2) or (2 in c and numJ == 1) or (NoJ.count(1) == 2 and numJ == 2):
        return 3

    # 1 pair
    elif (2 in c and c.count(2) == 1) or (numJ == 1):
        return 2

    # high card
    else:
        return 1 

def compareHand(hand1,hand2):
    hand1,hand2 = hand1[0],hand2[0]
 
    t1 = getType(countHand(hand1))
    t2 = getType(countHand(hand2))

    print(hand1,t1,hand2,t2)

    if t1 == t2:
        for i in range(len(hand1)):
            c1,c2 = hand1[i],hand2[i]
            if c1 != c2:
                return 1 if CARDS[c1] > CARDS[c2] else -1
    else:
        return 1 if t1 > t2 else -1

def main():
    Hands = readCards()
    Hands.sort(key=cmp_to_key(compareHand))
    
    ans = 0
    index = 1
    for h,w in Hands:
        ans += int(w) * index
        index += 1

    print(ans)



if __name__ == "__main__":
    main()
