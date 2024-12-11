from collections import defaultdict

with open("input", "r") as file:
    stones = [int(char) for char in file.readline().removesuffix("\n").split(" ")]

    blinks = 75
    i = 0
    map = defaultdict(int)
    for stone in stones:
        map[stone] += 1

    for i in range(blinks):
        aux = defaultdict(int)
        for k,v in map.items():
            aux[k] -= v
            s = str(k)

            if k == 0:
                aux[1] += v
            elif len(s) % 2 == 0:
                m = len(s) // 2
                l = s[:m]
                r = s[m:]
                aux[int(l)] += v
                aux[int(r)] += v
            else:
                aux[k*2024] += v
        for k, v in aux.items():
            map[k] += v
            if map[k] == 0:
                map.pop(k)

    print(sum(map.values()))
