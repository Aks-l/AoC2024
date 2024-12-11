with open("11/input11.txt") as file:
    nums = [int(x) for x in file.read().strip().split(" ")]

numCounter = {i:1 for i in nums}

for _ in range(75):
    print(_)
    working = {}
    lenght = len(numCounter)
    for i in numCounter.items():
        if i[0] == 0:
            if 1 not in working.keys(): working[1] = i[1]
            else: working[1] += i[1]

        elif len(str(i[0])) % 2 == 0:
            left = int(str(i[0])[len(str(i[0]))//2:])
            right = int(str(i[0])[:len(str(i[0]))//2])

            if left not in working.keys(): working[left] = i[1]
            else: working[left] += i[1]
            if right not in working.keys(): working[right] = i[1]
            else: working[right] += i[1]

        else:
            if i[0]*2024 not in working.keys(): working[i[0]*2024] = i[1]
            else: working[i[0]*2024] += i[1]

    numCounter = working

print(sum(numCounter.values()))