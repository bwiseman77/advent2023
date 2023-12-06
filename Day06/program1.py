#! /usr/bin/env python3
import sys

def main():
    Times = list(map(int,sys.stdin.readline().split(":")[1].split()))
    Dists = list(map(int,sys.stdin.readline().split(":")[1].split()))

    ans = 1
    for index, time in enumerate(Times):
        for held in range(time):
            dist = held*(time-held)
            if dist > Dists[index]:
                ans = ans * ( (time-held) - (held) + 1)
                break

    print(ans) 

if __name__ == "__main__":
    main()
