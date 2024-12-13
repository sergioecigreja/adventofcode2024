from collections import defaultdict

def dfs(field, i, j, plot, seen, group):
    if i < 0 or i >= len(field) or j < 0 or j >= len(field[0]):
        return
    if (i,j) in seen:
        return
    if field[i][j] != plot:
        return

    seen.add((i,j))
    group.add((i,j))
    dfs(field,i+1,j,plot, seen, group)
    dfs(field,i-1,j,plot, seen, group)
    dfs(field,i,j+1,plot, seen, group)
    dfs(field,i,j-1,plot, seen, group)

def countsides(region):
    sides = 0

    for plot in region:
        top = (plot[0]-1, plot[1])
        right = (plot[0], plot[1] + 1)
        left = (plot[0], plot[1] - 1)
        down = (plot[0] + 1, plot[1])

        if top not in region and left in region and (plot[0]-1,plot[1]-1) not in region:
            sides += 1
        if down not in region and left in region and (plot[0]+1,plot[1]-1) not in region:
            sides += 1
        if left not in region and top in region and (plot[0]-1,plot[1]-1) not in region:
            sides += 1
        if right not in region and top in region and (plot[0]-1,plot[1]+1) not in region:
            sides += 1

    return sides

with open("input", "r") as file:
    field = [l.removesuffix("\n") for l in file.readlines()]

    map = defaultdict(list)
    seen = set([])
    for i in range(len(field)):
        for j in range(len(field[0])):
            if (i,j) not in seen:
                group = set([])
                dfs(field,i,j,field[i][j],seen,group)
                map[field[i][j]].append(group)

    res = 0
    res2 = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for k,v in map.items():
        for region in v:
            area = len(region)
            perimeter = 0
            for plot in region:
                for dr, dc in directions:
                    nr, nc = plot[0] + dr, plot[1] + dc
                    if nr < 0 or nr >= len(field) or nc < 0 or nc >= len(field[0]):
                        perimeter += 1
                    elif field[nr][nc] != field[plot[0]][plot[1]]:
                        perimeter += 1

            res += area * perimeter
            res2 += area * (perimeter - countsides(region))
    print(res)
    print(res2)
