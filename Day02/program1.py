#! /usr/bin/env python3
import sys

COLORS = ("red","green","blue")
MAX    = {"red":12,"green":13,"blue":14}

def main():
    total  = 0
    total2 = 0
    while line := sys.stdin.readline():
        Id, data = line.split(":")
        Id       = Id.split(" ")[1]
        data     = data.split(";")

        C = {'red':0,'blue':0,'green':0}

        for item in data:
            bags = [item.strip() for item in item.split(',')]      
            for bag in bags:
                num,color = bag.split(' ')
                C[color] = max(C[color],int(num))

        ADD = True
        for item in MAX:
            if C[item] > MAX[item]:
                ADD = False

        if ADD:
            total += int(Id)

        #prob 2
        total2 += C["red"]*C["green"]*C["blue"]
    print(total,total2)
        
if __name__ == "__main__":
    main()
