#! /usr/bin/env python3
import sys
import re
def readCards():
    Cards = []

    while line := sys.stdin.readline():
        _,nums = line.strip().split(':')
        mine,wins = nums.split("|")
        mine = mine.strip(" ").split(" ")
        wins = wins.strip(" ").split(" ")
        Cards.append([mine,wins,1])

    return Cards

def checkWinners(cards):
    for card in cards:
        score = 0
        for num in card[0]:
            if num in card[1] and num != '':
                score = 1 if score == 0 else score * 2

        yield score

def getCopies(cards):
    Num = 0
    for i, card in enumerate(cards): # process each card
        m = 0
        for num in card[0]:
            if num in card[1] and num != '':
                m += 1
            
        for n in range(m):
            try:
                cards[i+n+1][2] += int(cards[i][2])
            except:
                pass

        Num += 1*cards[i][2]
        
    return Num

def main():
    Cards = readCards()
    print(sum(checkWinners(Cards)), getCopies(Cards))

if __name__ == "__main__":
    main()
