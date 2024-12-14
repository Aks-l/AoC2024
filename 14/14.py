import numpy as np  
import re
from functools import reduce

data = []
maxX, maxY = 101, 103
pattern = r"-?\d+"

with open('14/input14.txt') as file:
    for line in file:
        x, y, vx, vy = map(int, re.findall(pattern, line))
        data.append((x, y, vx, vy))

def findend(x, y, vx, vy, seconds):
    # nympy array swaps (x,y) with (y,x) in visualization
    endX = (y + vy*seconds) % (maxY)
    endY = (x + vx*seconds) % (maxX)
    return (endX, endY)

for i in range(10000): #part 1 uses only i=100
    endpos = []
    grid = np.zeros((maxY, maxX), dtype=int)
    for j in range(len(data)):
        endpos.append(findend(data[j][0], data[j][1], data[j][2], data[j][3], i))
    for x,y in endpos:
        grid[x, y] += 1
    #cheese: assume the tree uses all robots, therefore none should overlap (tunred out to be wrong, but works regardless)
    if not np.any((grid > 1)):
        print(i)

        ''' part1
        quadrants = [grid[:maxY//2,:maxX//2],grid[maxY//2+1:, :maxX//2], grid[maxY//2+1:, maxX//2+1:], grid[:maxY//2, maxX//2+1:]]
        quadSums = [(np.sum(i)) for i in quadrants]
    print(reduce(lambda x, y: x*y, quadSums))
        '''