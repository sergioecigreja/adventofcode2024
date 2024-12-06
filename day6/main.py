from enum import Enum
import sys

sys.setrecursionlimit(10**6)

#recursion is unnecessary
def traverse(lines,i,j,res,l,r,d):
    if i == l or j == r or i == -1 or j == -1:
        return
    if lines[i][j] == "#":
        match d:
            case Direction.U:
                d = Direction.R
                j += 1
                i += 1
            case Direction.D:
                d = Direction.L
                j -= 1
                i -= 1
            case Direction.R:
                d = Direction.D
                i += 1
                j -= 1
            case Direction.L:
                i -= 1
                j += 1
                d = Direction.U
    else:
        if (i,j) not in res:
            res.append((i,j))
        match d:
            case Direction.U:
                i-=1
            case Direction.D:
                i+=1
            case Direction.R:
                j+=1
            case Direction.L:
                j-=1

    return traverse(lines, i, j, res, l, r, d)

def traverse2(lines,i,j,res,l,r,d,set):
    if i == l or j == r or i == -1 or j == -1:
        return

    print((i,j,d))
    #loop
    if (i,j,d) in set:
        res.append((i,j,d))
        return

    set.add((i,j,d))

    if lines[i][j] == "#":
        match d:
            case Direction.U:
                d = Direction.R
                j += 1
                i += 1
            case Direction.D:
                d = Direction.L
                j -= 1
                i -= 1
            case Direction.R:
                d = Direction.D
                i += 1
                j -= 1
            case Direction.L:
                i -= 1
                j += 1
                d = Direction.U
    else:
        match d:
            case Direction.U:
                i-=1
            case Direction.D:
                i+=1
            case Direction.R:
                j+=1
            case Direction.L:
                j-=1

    return traverse2(lines, i, j, res, l, r, d, set)

with open("sample", "r") as file:
    lines = [line.removesuffix("\n") for line in file.readlines()]
    res = []
    l = len(lines)
    r = len(lines[0])
    Direction = Enum("Direction",[('U',1), ('D',2), ('R',3), ('L',4)])
    for i in range(l):
        for j in range(r):
            if lines[i][j] == '^':
                res.append((i,j))
    startingLine,startingRow = res[0][0], res[0][1]
    traverse(lines, res[0][0], res[0][1], res, l, r, Direction.U)

    res2 = []
    for i in range(l):
        for j in range(r):
            if (i,j) in res:
                if lines[i][j] == ".":
                    lines[i] = lines[i][:j] + "#" + lines[i][j+1:]
                    s = set()
                    traverse2(lines, startingLine, startingRow, res2, l, r, Direction.U, s)
                    lines[i] = lines[i][:j] + "." + lines[i][j+1:]
    print(len(res2))
    print(res2)
