import numpy as np

with open("input.txt", "r") as f:
    data = np.array([list(line.replace("\n", "")) for line in f.readlines()])

XMAS = ["X", "M", "A", "S"]
SAMX = XMAS[::-1]

def diagCount(grid: np.array) -> int:
    count = 0
    for i in range(4, len(grid)+1):
        for j in range(4, len(grid[0])+1):
            if (np.diag(grid[i-4:i, j-4:j])==XMAS).all() or (np.diag(grid[i-4:i, j-4:j])==SAMX).all():
                count += 1
            if (np.diag(grid[i-4:i, j-4:j][::-1])==XMAS).all() or (np.diag(grid[i-4:i, j-4:j][::-1])==SAMX).all():
                count += 1
    return count

def colCount(grid: np.array) -> int:
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])-3):
            if (grid[i][j:j+4]==XMAS).all() or (grid[i][j:j+4]==SAMX).all():
                count += 1
    return count

def rowCount(grid: np.array) -> int:
    count = 0
    for i in range(len(grid)-3):
        for j in range(len(grid[0])):
            if (grid[i:i+4, j]==XMAS).all() or (grid[i:i+4, j]==SAMX).all():
                count += 1
    return count

total1 = diagCount(data) + rowCount(data) + colCount(data)
print("Part 1: ", total1)

MAS = XMAS[1:]
SAM = SAMX[:-1]

def diagCountX_MAS(grid: np.array) -> int:
    count = 0
    for i in range(3, len(grid)+1):
        for j in range(3, len(grid[0])+1):
            diag1 = (np.diag(grid[i-3:i, j-3:j])==MAS).all() or (np.diag(grid[i-3:i, j-3:j])==SAM).all()
            diag2 = (np.diag(grid[i-3:i, j-3:j][::-1])==MAS).all() or (np.diag(grid[i-3:i, j-3:j][::-1])==SAM).all()
            if diag1 and diag2:
                count += 1
    return count

total2 = diagCountX_MAS(data)
print("Part 2: ", total2)