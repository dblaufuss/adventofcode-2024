#https://adventofcode.com/2024/day/2
data = []

with open("data\\day2.txt", "r") as f:
    for line in f.readlines():
        vals = [int(x) for x in line.split(" ")]
        data.append(vals)

safe_count = 0

def safetyTest(report: list) -> bool:
    for i in range(1, len(report)):
        if abs(report[i]-report[i-1]) > 3 or abs(report[i]-report[i-1]) == 0:
            return False
        if not (sorted(report) == report or sorted(report) == report[::-1]):
            return False
    return True

for i in range(len(data)):
    if safetyTest(data[i]):
        safe_count += 1

print("Part 1", safe_count)

safe_count = 0

for i in range(len(data)):
    for j in range(len(data[i])):
        if safetyTest(data[i][:j]+data[i][j+1:]):
            safe_count +=1
            break

print("Part 2", safe_count)
