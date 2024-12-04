
def get_all_diagonals(grid):
    size = len(grid)
    diagonals = []

    # Top-left to bottom-right (main diagonal direction)
    for start in range(size):  # Diagonals starting from top row
        diagonal = "".join(grid[i][i + start] for i in range(size - start))
        diagonals.append(diagonal)
    for start in range(1, size):  # Diagonals starting from first column
        diagonal = "".join(grid[i + start][i] for i in range(size - start))
        diagonals.append(diagonal)

    # Top-right to bottom-left (anti-diagonal direction)
    for start in range(size):  # Diagonals starting from top row
        diagonal = "".join(grid[i][size - 1 - i - start] for i in range(size - start))
        diagonals.append(diagonal)
    for start in range(1, size):  # Diagonals starting from last column
        diagonal = "".join(grid[i + start][size - 1 - i] for i in range(size - start))
        diagonals.append(diagonal)

    return diagonals

with open("input", "r") as file:
    lines = [s.strip('\n') for s in file.readlines()]
    res = 0
    for s in lines:
        for i in range(len(s)-3):
            if s[i:i+4] == "XMAS" or s[i:i+4] == "SAMX":
                res += 1

    columns = ["".join(column) for column in zip(*lines)]
    for s in columns:
        for i in range(len(s)-3):
            if s[i:i+4] == "XMAS" or s[i:i+4] == "SAMX":
                res += 1

    diag = get_all_diagonals(lines)
    for s in diag:
        for i in range(len(s)-3):
            if s[i:i+4] == "XMAS" or s[i:i+4] == "SAMX":
                res += 1

    res2 = 0
    for j in range(len(lines) -2):
        for i in range(len(lines) -2):
            if lines[j+1][i+1] == "A":
                if ((lines[j][i] == "M" and lines[j+2][i+2] == "S") or
                    (lines[j][i] == "S" and lines[j+2][i+2] == "M")):
                    if((lines[j+2][i] == "M" and lines[j][i+2] == "S") or
                        (lines[j+2][i] == "S" and lines[j][i+2] == "M")):
                        res2 += 1
    print(res2)
