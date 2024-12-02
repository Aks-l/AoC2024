output = 0
similar = 0

list1 = []
list2 = []

with open('1\input1.txt', 'r') as file:
    for line in file:
        vals = line.split("   ")
        list1.append(int(vals[0]))
        list2.append(int(vals[1]))

list1.sort()
list2.sort()

for i in range(len(list1)):
    output += abs(list1[i] - list2[i])
print(f"The difference is {output}")

for i in range(len(list1)):
    similar += list2.count(list1[i]) * list1[i]
print(f"The similarity is {similar}")

