import numpy as np

xmas = 0
directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

def checkXmas(i,j):
    xmas = 0
    for dx, dy in directions:
        if 0 <= i + 3*dx < rows and 0 <= j + 3*dy < columns:
            if lines[i+dx, j+dy] == "M":
                if lines[i+dx*2, j+dy*2] == "A":
                    if lines[i+dx*3, j+dy*3] == "S":
                        xmas+=1
    return xmas
    
def checkX_mas(i,j):
    xmas = 0
    if i>=1 and j>=1 and i<=rows-2 and j<=columns-2:
        cross = [lines[i+x,j+y] for x,y in directions[4::]]
        if cross.count("S") == 2 and cross.count("M") == 2:    #find correct corners 
            if lines[i-1, j-1] != lines[i+1, j+1]:             #avoid mam and sas
                xmas+=1
    return xmas

if __name__ == "__main__":
    with open("4/input4.txt", "r") as file:
        lines = np.array([list(line.strip()) for line in file])
        rows, columns = np.shape(lines)

    for i in range(rows):
        for j in range(columns):
            '''     part1
            if lines[i,j] == "X":
                xmas+=checkXmas(i,j)
            '''
            if lines[i,j] == "A":
                xmas+=checkX_mas(i,j)
    print(xmas)