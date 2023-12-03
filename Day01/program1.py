#! /usr/bin/env python3
import sys
import re

def main():

    NUMS  = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    num1  = 0
    num2  = 0
    total = 0 
    while line:=sys.stdin.readline():

        m    = re.findall(r"([0-9])|(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)",line)

        num1 = [n for n in m[0] if n != ''][0] 
        num2 = [n for n in m[-1] if n != ''][0] 

        if num1 in NUMS:
            num1 = NUMS[num1]

        if num2 in NUMS:
            num2 = NUMS[num2]

        total+= int(num1+num2)
 
    print(total)

if __name__ == "__main__":
    main()
