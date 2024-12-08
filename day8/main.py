from math import gcd
from collections import defaultdict

def validpoint(p, m):
    r = len(m)
    c = len(m[0])
    x, y = p
    if x >= 0 and x < r and y >= 0 and y < c:
       return True
    return False

def get_points(m, p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    points = []
    points.append(p1)
    points.append(p2)

    dx = x2 - x1
    dy = y2 - y1
    step_x = dx // gcd(abs(dx), abs(dy))
    step_y = dy // gcd(abs(dx), abs(dy))

    while True:
        before_p1 = (x1 - step_x, y1 - step_y)
        if validpoint(before_p1, m):
            points.append(before_p1)
            x1, y1 = before_p1
        else:
            break
    while True:
        after_p2 = (x2 + step_x, y2 + step_y)
        if validpoint(after_p2, m):
            points.append(after_p2)
            x2, y2 = after_p2
        else:
            break

    return points

with open("input", "r") as file:
    lines = [line.removesuffix("\n") for line in file.readlines()]
    map = defaultdict()
    sats = set([])
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] != '.':
                sat = lines[i][j]
                sats.add(sat)
                map[sat] = map.setdefault(sat, [])
                map.get(sat,[]).append((i,j))

    res = set([])
    for sat in sats:
        positions = map.get(sat, [])
        for i in range(len(positions)):
            p1 = positions[i]
            for p2 in positions[i+1:]:
                points = get_points(lines, p1, p2)
                for p in points:
                    res.add(p)
    print(len(res))

'''
for sat in sats:
    positions = map.get(sat, [])
    for i in range(len(positions)):
        p1 = positions[i]
        for p2 in positions[i+1:]:
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            an1 = (p1[0] + dx, p1[1] + dy)
            an2 = (p1[0] - dx, p1[1] - dy)
            if validpoint(an1,lines):
                res.add(an1)
            if validpoint(an2, lines):
                res.add(an2)
'''
