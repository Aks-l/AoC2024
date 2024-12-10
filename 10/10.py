import numpy as np

directions = [(0,1), (1,0), (0,-1), (-1,0)]
total = 0 

def findPaths(start, height, tempGrid):
    x,y = start
    paths = 0
    for i in range(len(directions)):
        dx, dy = directions[i]
        if 0 <= x+dx < len(tempGrid) and 0 <= y+dy < len(tempGrid):
            if int(tempGrid[x+dx,y+dy]) == height + 1:
                if height+1 == 9:
                    paths += 1
                    #tempGrid[x+dx, y+dy] = "0"  #uncomment for part 1
                else:
                    paths += findPaths((x+dx, y+dy), height + 1, tempGrid)
    return paths

with open("10/input10.txt", "r") as file:
    grid = np.array([[char for char in line] for line in file.read().splitlines()])
    starts = np.where(grid == "0")
    starts = list(zip(starts[0], starts[1]))

for i in starts:
    tempGrid = grid.copy()
    total += findPaths(i, 0, tempGrid)
print(total)