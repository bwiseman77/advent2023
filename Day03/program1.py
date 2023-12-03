#! /usr/bin/env python3
import sys

def check(grid,y,x,num,stars):
    l = len(num)+1
    # check end and front
    if grid[y][x-l] != '.' or grid[y][x] != '.':

        # check for stars
        if (x-l,y) in stars:
            stars[(x-l,y)].append(int(num))
        if (x,y) in stars:
            stars[(x,y)].append(int(num))
        return True

    # check top row
    for i, c in enumerate(grid[y-1][x-l:x+1]):
        if c != '.':
            if (x-l+i,y-1) in stars:
                stars[(x-l+i,y-1)].append(int(num))
            return True

    # check bottom row
    for i, c in enumerate(grid[y+1][x-l:x+1]):
        if c != '.':
            if (x-l+i,y+1) in stars:
                stars[(x-l+i,y+1)].append(int(num))
            return True
   
    return False

def findStars(grid,stars):
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == '*':
                stars[(x,y)] = []

def countGears(stars):
    gears = [stars[item] for item in stars if len(stars[item]) == 2]
    
    return sum([gear[0]*gear[1] for gear in gears])
        
def main():
    grid = ['.' + line.strip() + '.' for line in sys.stdin]
    grid = ['.'*len(grid[0])] + grid + ['.'*len(grid[0])]

    stars = {}

    Snum = ''
    Inum = 0
    Nums = []

    findStars(grid,stars)

    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c.isdigit():
                Snum += c
            else:
                if Snum != '':
                    if check(grid,i,j,Snum,stars):
                        print(f'{Snum}: True',end='\r\n')
                        Nums.append(int(Snum))
                    else:
                        print(f'{Snum}: False',end='\r\n')

                Snum = ''

    
    print(sum(Nums),countGears(stars))

if __name__ == "__main__":
    main()
