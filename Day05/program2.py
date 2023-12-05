#! /usr/bin/env python3
import sys
import re

def getMaps():
    Maps  = []
    index = 0
    Map   = list(map(int,re.findall(r'(\d+)\ ?',sys.stdin.readline())))    
    while line := sys.stdin.readline():
        if not line.strip():
            Maps.append(Map)
            index += 1
            Map = []
            continue

        if not line[0].isdigit():
            continue

        Map.append(list(map(int,re.findall(r'(\d+)\ ?',line))))

    Maps.append(Map)
    return Maps

def checkLoc(dest, lvl, Maps):

    # reached seeds
    if lvl == 0:
        seeds = Maps[0]
        for index in range(0,len(seeds)//2,2):
            if seeds[index] <= dest <= seeds[index]+seeds[index+1]:
                return dest
        return -2

    ans = -1
    for d,s,r in Maps[lvl]:

        # do we have mapping
        if d <= dest < d + r:
            ans = checkLoc(s+(dest-d),lvl-1,Maps)

    # didnt find, so pass down
    if ans == -1:
        ans = checkLoc(dest,lvl-1,Maps)

    return ans

def main():
    Maps = getMaps()

    i = 0
    while 1:
        if checkLoc(i,len(Maps)-1,Maps) > 0:
            print(i)
            return
        i += 1

if __name__ == "__main__":
    main()
