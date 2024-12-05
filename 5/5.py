rules = []
pages = []
output = 0

def fixPage(page):
    while True:
        fixRequired = False 
        for _ in page: 
            for key1, key2 in rules:
                if key1 in page and key2 in page: 
                    #if it is unsorted, swap the ones placed wrongly
                    if page.index(key1) > page.index(key2):  
                        page.pop(page.index(key1))
                        page.insert(page.index(key2), key1)
                        fixRequired = True 

        if not fixRequired:  
            break
    return page

def testPage(page):
    rulesMet = set() 
    for number in page:
        for rule in rules:
            key1, key2 = rule  
            if number == key1:
                rulesMet.add(key1)

            if number == key2 and key1 in page:
                if key1 not in rulesMet:
                    page = fixPage(page)
                    middle = int(page[len(page) // 2])
                    return middle
    return 0
    '''         part1
                    return 0
    
    middle = int(page[len(page) // 2])
    return middle
    '''
    
with open("5/input5.txt", "r") as file:
    for line in file:
        if line.strip() == "":
            continue
        elif "|" in line:
            rules.append(line.strip().split("|"))
        else:
            pages.append(line.strip().split(','))

for page in pages:
    output += testPage(page)

print(output)
