num_rules = 1176
num_updates = 203

rules = {}
updates = []

with open("input.txt", "r") as f:
    for rule in f.readlines()[0:num_rules]:
        num1 = int(rule[0:2])
        num2 = int(rule[3:5])
        try:
            rules[num1].append(num2)
        except KeyError:
            rules[num1] = [num2]

with open("input.txt", "r") as f:
    for update in f.readlines()[-num_updates:]:
        updates.append(eval("["+update+"]"))

correct = []

def isValidUpdate(update: list) -> bool:
    valid = True
    for i in range(len(update)):
        try:
            for val in rules[update[i]]:
                if val in update[0:i]:
                    valid = False
                    break 
        except KeyError:
            continue
    return valid
    
for update in updates:
    if isValidUpdate(update):
        correct.append(update)
    
total1 = sum(x[len(x)//2] for x in correct)
print("Part 1:", total1)

def validateUpdate(update: list) -> list:
    if isValidUpdate(update):
        return update

    for i in range(len(update)):
        try:
            for val in rules[update[i]]:
                for j in range(len(update[0:i])):
                    if val == update[j]:
                        update[i], update[j] = update[j], update[i]
                        return validateUpdate(update)
        except KeyError:
            continue

fixed = []

for update in updates:
    if not isValidUpdate(update):
        fixed.append(validateUpdate(update))

total2 = sum(x[len(x)//2] for x in fixed)
print("Part 2:", total2)