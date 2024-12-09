import numpy as np

directions = [(-1, 0),(0, 1),(1, 0),(0, -1)]

def checkForLoop(gr):
    x, y = startx, starty
    trailGrid = np.zeros((MAXX, MAXY, len(directions)))
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
            if grid[i,j] == "X":
                grid[i,j] = "#"
                validObstacles += checkForLoop(grid)
                grid[i,j] = "X"

    print(validObstacles)

def part1():
    x, y = startx, starty
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
        startx, starty = np.argwhere(grid == "^")[0]

    part1()
    part2()
    