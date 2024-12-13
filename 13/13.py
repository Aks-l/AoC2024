import numpy as np
import re
coins = 0
pattern = r"\d+"

def findCheapest(ax, bx, ay, by, px, py):
    try:
        solution = np.linalg.solve([[ax, bx], [ay, by]], [px, py])
        na, nb = map(round, solution)
        # reverse to invalidate floating point errors
        if na*ax + nb*bx == px and na*ay + nb *by == py:
            return 3*na + nb
    except:
        return 0 
    return 0
    
with open("13/input13.txt") as file:
    while True:
        ax, ay = map(int, re.findall(pattern, file.readline()))
        bx, by = map(int, re.findall(pattern, file.readline()))
        px, py = map(int, re.findall(pattern, file.readline()))
        px += 10000000000000
        py += 10000000000000

        coins += findCheapest(ax, bx, ay, by, px, py)
        if not (file.readline()):
            break  
print(coins)
