#https://adventofcode.com/2024/day/1
list1 = []
list2 = []

with open("data\\day1.txt", "r") as f:
    for line in f.readlines():
        vals = line.split("   ")
        list1.append(int(vals[0]))
        list2.append(int(vals[1]))

# part 1
list1.sort()
list2.sort()

total = 0

for i in range(len(list1)):
    total += abs(list1[i]-list2[i])

print(total)

# part 2
list2_map = {}

for i in range(len(list1)):
    if list2[i] not in list2_map.keys():
        list2_map[list2[i]] = 1
    else:
        list2_map[list2[i]] += 1

similar = 0

for num in list1:
    if num in list2_map.keys():
        similar += num * list2_map[num]

print(similar)