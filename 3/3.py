import re

do = 1
solutions = []

pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
intpattern = r"\d+"

def mult(equation):
    nums = list(map(int, re.findall(intpattern, equation)))
    solutions.append(nums[0]*nums[1])

with open("3/input3.txt", "r") as file:
    matches = re.findall(pattern, file.read())
    for i in matches:
        match i[2]:
            case 'l':
                if do: mult(i)
                #mult(i)        #part 1
            case '(': do = 1
            case 'n': do = 0
            
print(sum(solutions))
