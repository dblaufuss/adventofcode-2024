import re

with open("input.txt", "r") as f:
    data = "".join(f.readlines())

total = 0

for a, b in re.findall(r"mul\((\d+),(\d+)\)", data):
    total += int(a) * int(b)

print("Part 1: ", total)

total = 0
enabled = True

for a, b, do, dont in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data):
    if do or dont:
        enabled = bool(do)
    else:
        total += int(a) * int(b) * enabled

print("Part 2: ", total)