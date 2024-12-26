with open("19/input19.txt", "r") as file:
    parts, results = file.read().split("\n\n")

parts = parts.split(", ")
results = results.split("\n")

parts.sort()
out = 0

memory = {}

def possible(result):
    if result in memory:
        return memory[result]

    if len(result) == 0:
        return 1

    count = 0
    for part in parts:
        if result.startswith(part):
            count += possible(result[len(part):])

    memory[result] = count
    return count

for result in results:
    print(result)
    out += possible(result)

print(out)