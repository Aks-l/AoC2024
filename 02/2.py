def checkIfSafe(level):
    asc, dec = 0, 0
    for i in range(1, len(level)):

        if level[i-1] > level[i]: dec=1
        if level[i-1] < level[i]: asc=1
        if asc and dec: return 0

        if not (1 <= abs(level[i-1] - level[i]) <= 3):
            return 0
    return 1

def oneRemoved(level):
    results = []
    for i in range(len(level)):
        newlevel = level[:i] + level[i+1:]
        results.append(newlevel)
    return results

output = 0  

if __name__ == "__main__":
    with open('2\input2.txt', 'r') as file:
        for line in file:
            line = line.strip().split(" ")
            line = list(map(int, line))

            #if checkIfSafe(line): output+=1 #Part 1

            if any(checkIfSafe(l) for l in oneRemoved(line)): output+=1

    print(output)
