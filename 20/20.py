import numpy as np

with open("20/input20.txt", "r") as file:
    grid = np.array([list(line.strip()) for line in file], dtype=object)

directions = [(0,1), (1,0), (0,-1), (-1,0)]
locations = set()
maxX, maxY = grid.shape
cheatLength = 20 # set to 2 for part 1

def numify(grid):
    x,y = np.where(grid == "S")
    x,y = map(int, (x[0], y[0]))
    counter = 0
    while 1:
        grid[x,y] = counter
        locations.add((x,y))
        counter += 1
        for dx,dy in directions:
            if grid[x+dx,y+dy] == "E":
                locations.add((x+dx,y+dy))
                grid[x+dx,y+dy] = counter
                return grid
            if grid[x+dx,y+dy] == ".":
                x += dx
                y += dy
                break
            
grid = numify(grid)
grid = np.where(grid == "#", float("-inf"), grid)
out = 0

for x,y in locations:
    for i in range(-cheatLength,cheatLength+1):
        for j in range(-(cheatLength-abs(i)), cheatLength+1-abs(i)):
            if 0<=x+i<maxX and 0<=y+j<maxY:
                if grid[x+i,y+j] - grid[x,y] - abs(i) - abs(j) >= 100:
                    out+=1
print(out)
