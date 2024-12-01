import bisect

with open("input", 'r') as file:
    content = file.readlines()
    left = []
    right = []
    for line in content:
        values = line.split("  ")
        l = int(values[0])
        r = int(values[1])
        bisect.insort(left, l)
        bisect.insort(right, r)

    distance = sum([abs(l-r) for l,r in zip(left, right)])
    

#part 2
    countmap = {}
    for val in right:
        countmap[val] = right.count(val)
    
    similarity_score = sum(x * countmap.get(x, 0) for x in left)
    print(similarity_score)

