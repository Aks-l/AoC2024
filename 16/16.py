import numpy as np

with open("16/input16.txt", "r") as file:
    grid = np.array([list(line.strip()) for line in file.readlines()])

maxX, maxY = grid.shape
start = np.argwhere(grid == "S")[0]
end = np.argwhere(grid == "E")[0]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dijkstra():
    notSeen = [(0, start[0], start[1], 0)]  # cost, x, y, direction_index
    seen = set()

    gCost = np.full((maxX, maxY, len(directions)), np.inf)
    previous = {}

    for i in range(len(directions)):
        gCost[start[0], start[1], i] = 0

    while notSeen:
        current = min(notSeen)
        notSeen.remove(current)
        cost, x, y, dirIndex = current

        if (x, y) == tuple(end):
            path = [(x, y)]
            while (x, y, dirIndex) in previous:
                x, y, dirIndex = previous[(x, y, dirIndex)]
                path.append((x, y))
            return cost, path[::-1]

        seen.add((x, y, dirIndex))

        for i in range(len(directions)):
            dx, dy = directions[i]
            nx, ny = x + dx, y + dy

            if 0 <= nx < maxX and 0 <= ny < maxY and grid[nx, ny] != "#":
                turnCost = 1 if i == dirIndex else 1001
                newCost = gCost[x, y, dirIndex] + turnCost

                if newCost < gCost[nx, ny, i]:
                    gCost[nx, ny, i] = newCost
                    notSeen.append((newCost, nx, ny, i))
                    previous[(nx, ny, i)] = (x, y, dirIndex)

    return float('inf'), []

cost, optimalPath = dijkstra()

optimalCost = cost

seats = [_ for _ in optimalPath]

for coord in optimalPath:
    grid[coord] = "#"
    newCost, newPath = dijkstra()
    if newCost == optimalCost:
        for newCoord in newPath:
            if newCoord not in seats:
                seats.append(newCoord)
    grid[coord] = "."  
print(len(seats))
