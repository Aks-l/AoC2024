disk = []

def part1():
    lPtr = 0
    rPtr = len(disk)-1

    while lPtr < rPtr:
        if disk[lPtr] != ".":
            lPtr += 1
            continue 
        if disk[rPtr] == ".":
            rPtr -= 1
            continue  

        disk[lPtr], disk[rPtr] = disk[rPtr], disk[lPtr]
        lPtr += 1
        rPtr -= 1

def part2():
    lPtr = 0
    rPtr = len(disk)-1
    while rPtr > 0:
        # Find next number and length of consecutive numbers
        if disk[rPtr] == ".":
            rPtr -= 1
            continue
        else: 
            seqNum = 1
            number = disk[rPtr]
            while rPtr - seqNum >= 0 and disk[rPtr - seqNum] == number: seqNum += 1

        # Find big enough cluster of dots
        placeFound = False
        while not placeFound:
            while lPtr < rPtr and disk[lPtr] != ".": lPtr += 1
            seqDot = 1
            while lPtr + seqDot < rPtr and disk[lPtr + seqDot] == ".": seqDot += 1
            if seqDot >= seqNum: placeFound = True
            else:
                if lPtr + seqDot >= rPtr: break
                else: lPtr += seqDot

        # Swap if dot-cluster was found
        if placeFound:
            disk[lPtr : lPtr+seqNum], disk[rPtr-seqNum+1 : rPtr+1] = disk[rPtr-seqNum+1 : rPtr+1], disk[lPtr : lPtr+seqNum]
            rPtr -= seqNum
            lPtr = 0
        else: 
            rPtr -= 1
    
if __name__ == "__main__":
    with open("9/input9.txt", "r") as file:
        data = [int(char) for char in file.readline()]
        
    for i in range(len(data)):
        if i % 2 == 1: disk.extend(["."] * int(data[i])) 
        else: disk.extend([str(i // 2)] * int(data[i]))

    #part1()
    part2()

    sum = 0
    for i in range(len(disk)):
        if disk[i] != ".":
            sum += int(disk[i])*i
    print(sum)