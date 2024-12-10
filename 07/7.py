'''
Explanation:
for each set of numbers, a ternary grid is made to create each combination 
of operators (it gets exponentially slower for each operator possible). 
Then for each combination, they are applied in left to right order.
If it equals the needed result, it is added to the total sum.
'''


def base3(num):
    if num == 0:
        return "0"
    digits = []
    while num > 0:
        digits.append(str(num % 3))
        num //=3
    return ''.join(reversed(digits))

def addOperators(num, length):
    ret = base3(num).zfill(length)
    return ret.replace("0", "+").replace("1", "*").replace("2", "|")

def possibleSums(values):
    nums = list(map(int, values.split(" ")))
    opCount = len(nums) - 1
    if opCount < 1:
        return nums

    operatorSets = [addOperators(i, opCount) for i in range(3**opCount)]

    ret = []
    for opSet in operatorSets:
        working = nums[:]  
        
        for symbol in opSet:
            a = working[0]
            b = working[1]
            if symbol == "|":
                res = a * (10**len(str(b))) + b
            elif symbol == "+":res = a + b
            else: res = a * b
            working[0] = res 
            working.pop(1)
        ret.append(working[0])
    return ret


if __name__ == "__main__":
    with open("input7.txt", "r") as file:
        ans = 0
        conprehended = 0
        for line in file:
            answer, nums = line.strip().split(": ")
            answer = int(answer)
            if answer in possibleSums(nums):
                ans += answer
            print(conprehended)
            conprehended += 1

    print(ans)

