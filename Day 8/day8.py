import numpy as np

with open("input.txt", "r") as f:
    data = np.array([list(line.strip()) for line in f.readlines()])

nodes = {}
anti_nodes = set()
extra_nodes = set()

for row, col in np.ndindex(data.shape):
    if data[row, col] == ".":
        continue
    try:
        nodes[data[row, col]].append((row, col))
    except KeyError:
        nodes[data[row, col]] = [(row, col)]

def validate_anti(anti) -> bool:
    if any(x < 0 for x in anti):
        return False
    try:
        if data[*anti]:
            return True
    except IndexError:
        return False

for key in nodes:
    freq = nodes[key]
    if len(freq) <= 1:
        continue
    for i in range(len(freq)):
        for j in range(i+1, len(freq)):
            extra_nodes.add((freq[i][0], freq[i][1]))
            extra_nodes.add((freq[j][0], freq[j][1]))

            d_row = freq[j][0]-freq[i][0]
            d_col = freq[j][1]-freq[i][1]

            anti1 = [freq[j][0]+d_row, freq[j][1]+d_col]

            if validate_anti(anti1):
                anti_nodes.add(tuple(anti1))

            while True:
                anti1[0] += d_row
                anti1[1] += d_col
                if validate_anti(anti1):
                    extra_nodes.add(tuple(anti1))
                else:
                    break

            anti2 = [freq[i][0]-d_row, freq[i][1]-d_col]

            if validate_anti(anti2):
                anti_nodes.add(tuple(anti2))

            while True:
                anti2[0] -= d_row
                anti2[1] -= d_col
                if validate_anti(anti2):
                    extra_nodes.add(tuple(anti2))
                else:
                    break

print("Part 1:", len(anti_nodes))
print("Part 2:", len(anti_nodes | extra_nodes))