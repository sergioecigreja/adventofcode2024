with open("input", "r") as file:
    line = file.readline().removesuffix("\n")

    onfile = True
    j = 0
    id = 0
    memory = []
    for i in range(len(line)):
        if onfile:
            file = int(line[i])
            for k in range(file):
                memory.append(id)
            j += file
            id += 1
            onfile = False
        else:
            empty = int(line[i])
            for k in range(empty):
                memory.append('.')
            j += empty
            onfile = True

    refrag = []
    i = 0
    j = len(memory) -1
    while(i <= j):
        if memory[i] == "." and memory[j] != ".":
            refrag.append(memory[j])
            i += 1
            j -= 1
        elif memory[i] != ".":
            refrag.append(memory[i])
            i += 1
        elif memory[j] == ".":
            j -= 1

    res = 0
    for i in range(len(refrag)):
        res += i * refrag[i]

    #part2
    spaces = []
    start = -1
    end = -1
    for i in range(len(memory)):
        if memory[i] == ".":
            if start != -1:
                end = i
            else:
                start = i
                end = i
        else:
            if start != -1:
                spaces.append((end - start + 1, start, end))
                start = -1
                end = -1

    blocks = []
    start_index = 0
    for i, f in enumerate(memory):
        if not blocks or f != memory[i - 1]:
            if blocks:
                blocks[-1] = (blocks[-1][0], blocks[-1][1], i - 1)
            blocks.append(([f], i, None))
            start_index = i
        else:
            blocks[-1][0].append(f)
    if blocks:
        blocks[-1] = (blocks[-1][0], blocks[-1][1], len(memory) - 1)

    replace=lambda a,b,s:a[:s]+b+a[s+len(b):]
    for block in blocks[::-1]:
        if block[0][0] != ".":
            for i in range(len(spaces)):
                space = spaces[i]
                if space[0] >= len(block[0]) and space[1] < block[1]:
                    memory = replace(memory, block[0], space[1])
                    memory = replace(memory, ["."]*len(block[0]), block[1])
                    space = (space[0] - len(block[0]),space[1]+len(block[0]), space[2])
                    spaces[i] = space
                    break

    res2 = 0
    for i in range(len(memory)):
        if(memory[i] != "."):
            res2 += i * memory[i]
    print(res2)
