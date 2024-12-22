prune = 16777216
output = 0

def first(num):
    mix = num * 64
    return (num ^ mix) % prune
def second(num):
    mix = num // 32
    return (num ^ mix) % prune
def third(num):
    mix = num * 2048
    return (num ^ mix) % prune

_input = []

with open("22/input22.txt") as file:
    _input = [int(line.strip()) for line in file]

lines = len(_input)

allChangeSec = []
allLastSec = []
for num in _input:
    working = num
    change_seq = [0]
    last_seq = [0]
    for _ in range(2000):
        working = first(working)
        working = second(working)
        working = third(working)
        output += working

        last = int(str(working)[-1])
        change_seq.append(last - last_seq[-1])
        last_seq.append(last)

    allChangeSec.append(change_seq)
    allLastSec.append(last_seq)

highest = 0

# Brute force the sequence
for a in range(-3, 4):
    for b in range(-3, 4):
        for c in range(-3, 4):
            for d in range(-3, 4):
                bananas = 0
                seq = [a, b, c, d]

                for i in range(lines):
                    for j in range(len(allChangeSec[i]) - len(seq) + 1):
                        if allChangeSec[i][j:j + len(seq)] == seq:
                            bananas += allLastSec[i][j + 3]
                            break

                if bananas > highest:
                    highest = bananas
                    print(f"Most bananas: {bananas} at {seq}")
print(highest)