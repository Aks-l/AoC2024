import numpy as np

grid = np.zeros((71, 71), dtype=str)
maxX, maxY = grid.shape
start = (0, 0)
end = (70, 70)

with open("18/input18.txt", "r") as file:
    lines = file.readlines()

coords = []
for i in lines:
    i = i.strip().split(",")
    coords.append([int(i[0]), int(i[1])])

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dijkstra():
    notSeen = [(0, start[0], start[1])]  # cost, x, y, direction_index
    seen = set()

    gCost = np.full((maxX, maxY), np.inf)
    previous = {}

    for i in range(len(directions)):
        gCost[start[0], start[1]] = 0

    while notSeen:
        current = min(notSeen)
        notSeen.remove(current)
        cost, x, y = current

        if (x, y) == tuple(end):
            path = [(x, y)]
            while (x, y) in previous:
                x, y = previous[(x, y)]
                path.append((x, y))
            return cost, path[::-1]

        seen.add((x, y))

        for i in range(len(directions)):
            dx, dy = directions[i]
            nx, ny = x + dx, y + dy

            if 0 <= nx < maxX and 0 <= ny < maxY and grid[nx, ny] != "1":
                turnCost = 1
                newCost = gCost[x, y] + turnCost
                
                if newCost < gCost[nx, ny]:
                    gCost[nx, ny] = newCost
                    notSeen.append((newCost, nx, ny))
                    previous[(nx, ny)] = (x, y)
    return float('inf'), []

for x, y in coords: #should start at 1024, but nah
    grid[y, x] = 1
    if dijkstra()[0] == float('inf'):
        print(x,y)
        break

'''
part 1 at coord index 1024:
path = dijkstra()[1]
print(len(path))
'''