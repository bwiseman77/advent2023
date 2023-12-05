#! /usr/bin/env python3
import sys
import re

def getMaps():
    Maps  = []
    index = 0
    Map   = re.findall(r'(\d+)\ ?',sys.stdin.readline())
    
    while line := sys.stdin.readline():
        if not line.strip():
            Maps.append(Map)
            index += 1
            Map = []
            continue

        if not line[0].isdigit():
            continue

        Map.append(re.findall(r'(\d+)\ ?',line))

    Maps.append(Map)
    return Maps

def checkSeed(source, lvl, Maps):
    if lvl == len(Maps):
        return source

    ans = -1
    for d,s,r in Maps[lvl]:
        d,s,r = int(d),int(s),int(r)

        # yes
        if source >= s and source < s + r:
            ans = checkSeed(d+(source-s),lvl+1,Maps)

    if ans == -1:
        ans = checkSeed(source,lvl+1,Maps)

    return ans

def main():
    Maps = getMaps()

    ans = float('inf')
    for seed in Maps[0]:
        ans = min(checkSeed(int(seed),1,Maps), ans)
        
    print(ans)

if __name__ == "__main__":
    main()
