import numpy as np
from copy import deepcopy

directions = [(-1, 0),(0, 1),(1, 0),(0, -1)]

def checkForLoop(gr):
    x, y = int(np.where(gr == "^")[0]), int(np.where(gr == "^")[1])
    trailGrid = np.zeros((MAXX, MAXY, 4))
    direction = 0
    dx,dy = directions[direction]
    while 1:
        if trailGrid[x,y,direction] == 1:
            return 1
        if x+dx < 0 or x+dx >= MAXX or y+dy < 0 or y+dy >= MAXY:
            return 0
        while gr[x+dx, y+dy] == "#":
            direction = (direction + 1) % 4
            dx,dy = directions[direction]
        trailGrid[x,y,direction] = 1
        x += dx
        y += dy

def part2():
    validObstacles = 0
    for i in range(MAXX):
        for j in range(MAXY):
            tempgrid = deepcopy(grid)
            if tempgrid[i,j] == ".":
                tempgrid[i,j] = "#"
                validObstacles += checkForLoop(tempgrid)
    print(validObstacles)

def part1():
    x, y = int(np.where(grid == "^")[0]), int(np.where(grid == "^")[1])
    direction = 0
    while 0 <= x <= MAXX and 0 <= y <= MAXY:
        dx,dy = directions[direction]
        if x+dx < 0 or x+dx >= MAXX or y+dy < 0 or y+dy >= MAXY:
            grid[x,y] = "X"
            break   
        while grid[x+dx, y+dy] == "#":
            direction = (direction + 1) % 4
            dx,dy = directions[direction]
        grid[x,y] = "X"
        x += dx
        y += dy
    print(np.sum(grid == "X"))

if __name__ == "__main__":
    with open("6/input6.txt", "r") as file:
        lines = file.readlines()
        grid = np.array([list(line.strip()) for line in lines])
        MAXX, MAXY = grid.shape

    #part1 changes the grid, part2 creates copies so it runs first
    part2()
    part1()