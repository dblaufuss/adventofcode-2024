import numpy as np

data = []

with open("data\\day6.txt", "r") as f:
    for line in f.readlines():
        data.append([*line.strip()])

data = np.array(data)
guard_start = tuple(np.array(np.where(data=="^"))[:, 0])

def walk(grid):
    guard_pos = list(np.array(np.where(grid=="^"))[:, 0])
    direction = "^"
    seen = set()
    positions = set()
    positions.add(tuple([*guard_pos, direction]))
    loop = False

    while True:
        try:
            if direction == "^":
                while grid[guard_pos[0], guard_pos[1]] != "#":
                    seen.add(tuple(guard_pos))
                    if guard_pos[0]-1 < 0:
                        raise IndexError
                    guard_pos[0] -= 1
                guard_pos[0] += 1
                direction = ">"

            elif direction == ">":
                while grid[guard_pos[0], guard_pos[1]] != "#":
                    seen.add(tuple(guard_pos))
                    guard_pos[1] += 1
                guard_pos[1] -= 1
                direction = "V"

            elif direction == "V":
                while grid[guard_pos[0], guard_pos[1]] != "#":
                    seen.add(tuple(guard_pos))
                    guard_pos[0] += 1
                guard_pos[0] -= 1
                direction = "<"

            else:
                while grid[guard_pos[0], guard_pos[1]] != "#":
                    seen.add(tuple(guard_pos))
                    if guard_pos[1]-1 < 0:
                        raise IndexError
                    guard_pos[1] -= 1
                guard_pos[1] += 1
                direction = "^"

        except IndexError:
            break
        
        if tuple([*guard_pos, direction]) in positions:
            loop = True
            break

        positions.add(tuple([*guard_pos, direction]))

    return seen, loop

path = walk(data)[0]

print("Part 1:", len(path))

total = 0

for pos in path:
    if pos == guard_start:
        continue
    new_grid = data.copy()
    new_grid[pos[0], pos[1]] = "#"
    if walk(new_grid)[1] == True:
        total += 1

print("Part 2:", total)