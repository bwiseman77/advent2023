#! /usr/bin/env python3
import sys

def main():
    Time = int(("").join(sys.stdin.readline().split(":")[1].split()))
    Dist = int(("").join(sys.stdin.readline().split(":")[1].split()))


    for held in range(Time):
        dist = held*(Time-held)
        if dist > Dist:
            print(((Time-held) - (held) + 1))
            break

if __name__ == "__main__":
    main()
