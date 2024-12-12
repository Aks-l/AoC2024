import numpy as np
from matrixToEdges import uniqueMatrices 

def mirror_rotate(matrix):
    variants = []
    mat = np.array(matrix)
    for _ in range(4):
        variants.append(tuple(map(tuple, mat)))
        variants.append(tuple(map(tuple, np.fliplr(mat))))
        mat = np.rot90(mat)
    return variants

# convert matrix to that matrix, but letter -> 1, other -> 0
def find3x3(origMatrix, letter):
    boolMatrix = []
    for row in origMatrix:
        boolRow = []
        for cell in row:
            boolRow.append(1 if cell == letter else 0)
        boolMatrix.append(tuple(boolRow))
    boolMatrix = tuple(boolMatrix)

    variants = mirror_rotate(boolMatrix)

    for variant in variants:
        if variant in uniqueMatrices:
            return uniqueMatrices[variant]
    return 0

def findCircum(x, y, grid, letter, visited):
    if not (0 <= x < maxX and 0 <= y < maxY): return 0
    if grid[x, y] != letter or (x, y) in visited: return 0

    visited.add((x, y))
    circum = 0

    '''      part 1
    for dx, dy in adjacent:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < maxX and 0 <= ny < maxY) or grid[nx, ny] != letter:
            circum += 1
        else:
            circum += findCircum(nx, ny, grid, letter, visited)
    '''
    surrounding3x3 = []
    for dx in [-1, 0, 1]:
        row = []
        for dy in [-1, 0, 1]:
            if 0 <= x+dx < maxX and 0 <= y+dy < maxY:
                row.append(grid[x+dx, y+dy])
            else:
                row.append('.') 
        surrounding3x3.append(row)

    checkMatrix = surrounding3x3

    circum += find3x3(checkMatrix, letter)

    for dx, dy in adjacent:
        circum += findCircum(x + dx, y + dy, grid, letter, visited)
    
    return circum

def findArea(x, y, grid, letter):
    if not (0 <= x < maxX and 0 <= y < maxY) or grid[x, y] != letter:
        return 0

    grid[x, y] = "."  
    area = 1 

    for dx, dy in adjacent:
        area += findArea(x + dx, y + dy, grid, letter)

    return area

adjacent = [(0, 1), (1, 0), (0, -1), (-1, 0)]

with open("12/input12.txt") as file:
    grid = np.array([[c for c in line.strip()] for line in file.readlines()])
    maxX, maxY = grid.shape

price = 0

totalArea = 0
totalCircum = 0

aGrid = np.copy(grid)
cGrid = np.copy(grid)

for i in range(maxX):
    for j in range(maxY):
        if aGrid[i, j] != ".": 
            letter = aGrid[i, j]
          
            area = findArea(i, j, aGrid, letter)
        
            visited = set() #instead og marking visited = ".", since we must not change what we are working with here
            circum = findCircum(i, j, cGrid, letter, visited)

            price += area * circum
    print(f"{i}/{maxX}")
print(price)
