import numpy as np

directions = {">":(0, 1), "v":(1, 0), "<":(0, -1), "^":(-1, 0)}

def part1(x, y):
    for i in movements.strip():
        if i in "v^<>":
            dx, dy = directions[i]
            nx, ny = x + dx, y + dy
            if grid[nx, ny] == ".": x, y = nx, ny
            elif grid[nx, ny] == "#": continue
            else:
                nx, searcherY = nx, ny
                while True:
                    nx += dx
                    searcherY += dy
                    if grid[nx, searcherY] == "#":
                        break
                    if grid[nx, searcherY] == ".":
                        grid[nx, ny] = "."
                        grid[nx, searcherY] = "O"
                        x+=dx
                        y+=dy
                        break

def reshapeIntoPart2(x, grid):
    sizeX, sizeY = grid.shape
    newGrid = np.zeros((sizeX, sizeY * 2), dtype=str)
    for i in range(sizeX):
        for j in range(sizeY):
            if grid[i, j] == "#":
                newGrid[i, j*2 : j*2+2] = "#"
            elif grid[i, j] == "O":
                newGrid[i, j*2] = "["
                newGrid[i, j*2 + 1] = "]"
            else:
                newGrid[i, j*2 : j*2+2] = "."
    return newGrid
    
def findRestOfBox(boxX, boxY):
    if grid[boxX, boxY] == "[": return [boxX, boxY+1]
    else: return [boxX, boxY-1]
    
def part2(x, y):
    y*=2
    for i in movements:
        if i in "v^<>":
            dx, dy = directions[i]
            nx, ny = x + dx, y + dy
            if grid[nx, ny] == ".": 
                x, y = nx, ny
            elif grid[nx, ny] == "#":
                continue            
            else:
                if i in "<>":
                    marked = set()
                    searcherY = ny
                    while True:
                        searcherY += dy
                        if grid[nx, searcherY] == "#":
                            marked = set()
                            break
                        if grid[nx, searcherY] == ".":
                            
                            grid[nx, searcherY] = "[" if i == "<" else "]"
                            x += dx
                            y += dy
                            grid[x, y] = "."
                            break
                        if grid[nx, searcherY] == "[" or grid[nx, searcherY] == "]":
                            marked.add(int(searcherY))
                    for yVal in marked:
                        grid[x,yVal] = "[" if grid[x,yVal] == "]" else "]"
                if i in "v^":
                    connected = [[nx, ny], findRestOfBox(nx, ny)]
                    for a, b in connected:
                        if grid[a+dx, b] == "[" or grid[a+dx, b] == "]":
                            connected.extend([[a+dx, b], findRestOfBox(a+dx, b)])
                            
                    if any(grid[a+dx, b] == "#" for a, b in connected):
                        continue

                    connected = list(set((int(a), int(b)) for a, b in connected))
                    if dx < 0:
                        connected.sort()
                    else:
                        connected.sort(reverse=True)
                    
                    for a, b in connected:
                        grid[a + dx, b] = grid[a, b]
                        grid[a, b] = "."
                    x, y = nx, ny

with open("15/input15.txt", "r") as file:
    grid, movements = file.read().split("\n\n")
    grid = np.array([list(row) for row in grid.split("\n")])
    sizeX, sizeY = grid.shape
    x, y = np.where(grid == "@")
    grid[x, y] = "."
    #part1(x, y)
    grid = reshapeIntoPart2(x, grid)
    part2(x, y)

#allO = np.where(grid == "O")
allO = np.where(grid == "[")
print(100*sum(allO[0]) + sum(allO[1]))

