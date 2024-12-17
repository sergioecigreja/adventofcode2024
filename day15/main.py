from enum import Enum

class Direction(Enum):
    N = '^'
    S = 'v'
    E = '>'
    W = '<'

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"{self.x} {self.y}"

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

def to_point(i, j, direction:Direction)->Point:
    match direction:
        case Direction.N:
            return Point(i-1,j)
        case Direction.S:
            return Point(i+1, j)
        case Direction.E:
            return Point(i, j+1)
        case Direction.W:
            return Point(i, j-1)

def can_navigate(r,d,map):
    if map[r.x][r.y] == "#":
        return -1
    np = to_point(r.x, r.y, d)
    depthL = 0
    depthR = 0

    if map[np.x][np.y] == "#":
        return -1
    if map[np.x][np.y] == "[":
        if d == Direction.N or d == Direction.S:
            depthL += can_navigate(np,d,map)
            if depthL != 0:
                depthR  += can_navigate(Point(np.x, np.y + 1), d, map)
            else:
                return -1
            if depthL == -1 or depthR == -1 or depthL != depthR:
                return -1
            return depthL
        else:
            return -1 #shouldn't get here, will only use if north or south
    if map[np.x][np.y] == "]":
        if d == Direction.N or d == Direction.S:
            depthR += can_navigate(np,d,map)
            if depthR != 0:
                depthL  += can_navigate(Point(np.x, np.y - 1), d, map)
            else:
                return -1
            if depthL == -1 or depthR == -1 or depthL != depthR:
                return -1
            return depthL
        else:
            return -1 #shouldn't get here, will only use if north or south
    if map[np.x][np.y] == ".":
        return 1

    return -1

def navigate(r, d, map):
    if map[r.x][r.y] == "#":
        return
    np = to_point(r.x, r.y, d)

    if map[np.x][np.y] == "#":
        return r
    if map[np.x][np.y] == "O":
        navigate(np,d,map)
    if map[np.x][np.y] == "[":
        if d == Direction.N or d == Direction.S:
            depth = can_navigate(r, d, map)
            if (depth == -1):
                return r
            p = navigate(np,d,map)
            if p != np:
                a = Point(np.x, np.y + 1)
                b = navigate(a, d, map)
                if a == b:
                    c = to_point(np.x, np.y, d)
                    map[np.x] = map[np.x][:np.y] + map[c.x][c.y] + map[np.x][np.y+1:]
                    map[c.x] = map[c.x][:c.y] + "." + map[c.x][c.y+1:]
        else:
            navigate(np, d, map)

    if map[np.x][np.y] == "]":
        if d == Direction.N or d == Direction.S:
            depth = can_navigate(r, d, map)
            if (depth == -1):
                return r
            p = navigate(np,d,map)
            if p != np:
                a = Point(np.x, np.y - 1)
                b = navigate(a, d, map)
                if a == b:
                    c = to_point(np.x, np.y, d)
                    map[np.x] = map[np.x][:np.y] + map[c.x][c.y] + map[np.x][np.y+1:]
                    map[c.x] = map[c.x][:c.y] + "." + map[c.x][c.y+1:]
        else:
            navigate(np,d,map)
    if map[np.x][np.y] == ".":
        map[np.x] = map[np.x][:np.y] + map[r.x][r.y] + map[np.x][np.y+1:]
        map[r.x] = map[r.x][:r.y] + '.' + map[r.x][r.y+1:]
        return np

    return r
with open("input", "r") as f:
    lines = [l.removesuffix("\n") for l in f.readlines()]
    map = []
    robot = []
    parsingrobot = False
    for l in lines:
        if l == "":
            parsingrobot = True
        elif parsingrobot:
            robot.append(l)
        else:
            map.append(l)

    valid = lambda p: 0<p.x<len(map) and 0<p.y<len(map[0])

    r = Point(-1,-1)
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "@":
                r = Point(i,j)
    '''
    for l in robot:
        for i in range(len(l)):
            d = Direction(l[i])
            r = navigate(r,d,map)
    '''
    res = 0
    for i in range(len(map)):
        print(map[i])
        for j in range(len(map[0])):
            if map[i][j] == "O":
                res += i*100 + j
    print(res)

    #part2
    robot = []
    parsingrobot = False
    map = []

    for l in lines:
        if l == "":
            parsingrobot = True
        elif parsingrobot:
            robot.append(l)
        else:
            list = []
            for i in range(len(l)):
                if l[i] == '@':
                    list.append("@")
                    list.append(".")
                if l[i] == ".":
                    list.append(".")
                    list.append(".")
                if l[i] == "#":
                    list.append("#")
                    list.append("#")
                if l[i] == "O":
                    list.append("[")
                    list.append("]")

            map.append("".join(list))
    for l in map:
        print(l)
    r = Point(-1,-1)
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "@":
                r = Point(i,j)

    for l in robot:
        for i in range(len(l)):
            if l[i] != "#":
                d = Direction(l[i])
                r = navigate(r,d,map)

    for l in map:
        print(l)
    w = len(map[0])
    h = len(map)
    res2 = 0
    for i in range(h):
        for j in range(w):
            if map[i][j] == "[":
                res2 += i * 100 + j
    print(res2)
