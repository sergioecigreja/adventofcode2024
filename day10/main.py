
def dfs(m,i,j,level,seen):
    if i >= len(m) or i < 0 or j >= len(m[0]) or j < 0:
        return 0
    if ((i,j) in seen):
        return 0
    curr = m[i][j]
    if curr != level:
        return 0
    elif curr == 9:
        seen.add((i,j))#Removed for part2
        return 1
    else:
        return dfs(m,i-1,j,level+1,seen) + dfs(m,i+1,j,level+1,seen) + dfs(m,i,j-1,level+1,seen) + dfs(m,i,j+1,level+1,seen)

with open("input", "r") as file:
    m = [line.removesuffix("\n") for line in file.readlines()]
    m = [[int(char) for char in s if char.isdigit()] for s in m]
    r = len(m)
    c = len(m[0])

    res = 0
    for i in range(r):
        for j in range(c):
            if m[i][j] == 0:
                seen = set([])
                res += dfs(m,i,j,0,seen)
    print(res)
