with open("input", "r") as file:
    lines = file.readlines()
    rules = []
    updates = []

    parsing = True
    for line in lines:
        if line == "\n":
            parsing = False
            continue
        if parsing:
            rules.append(line.removesuffix("\n"))
        else:
            updates.append(line.removesuffix("\n"))

    dict = {}
    for i in range(10, 100):
        dict[str(i)] = []

    for rule in rules:
        (a,b) = rule.split("|")
        dict[a].append(b)

    valid_updates = []
    invalid_updates = []
    for update in updates:
        pages = update.split(",")
        visited = set()
        res = True
        for page in pages:
            prev = dict[page]
            for p in prev:
                if p in visited:
                    res = False
                    break
            if not res:
                break
            visited.add(page)
        if res:
            valid_updates.append(update)
        else:
            invalid_updates.append(update)

    res = 0
    for valid in valid_updates:
        pages = valid.split(",")
        m = len(pages)//2
        res += int(pages[m])
    print(res)
    #part2
    res2 = 0
    for update in invalid_updates:
        pages = update.split(",")
        ranks = {}
        m = len(pages)//2
        for page in pages:
            prev = set(dict[page])
            rank = 0
            for p in pages:
                if p not in prev:
                    rank += 1
            if rank == m+1:
                res2 += int(page)
                break
    print(res2)
