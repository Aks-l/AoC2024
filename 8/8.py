import numpy as np

charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("8/input8.txt", "r") as file:
    grid = np.array([list(line.strip()) for line in file])
    antiGrid = np.zeros(grid.shape, dtype=bool)
    maxX, maxY = grid.shape

for char in charset:
    places = np.where(grid == char)
    pos = list(zip(places[0], places[1]))

    for x,y in pos:
        for x2, y2 in pos:
            dx, dy = x2-x, y2-y
            #part 2 just added this loop and the following i's:
            for i in range(maxX):
                if 0 <= x-dx*i < maxX and 0 <= y-dy*i < maxY:
                    antiGrid[x-dx*i, y-dy*i] = 1
                    #since it loops through the same pair in reverse later
                    #we don't mark the mirror now

print(np.count_nonzero(antiGrid))
