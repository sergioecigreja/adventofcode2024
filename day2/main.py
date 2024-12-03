
def isReportSafe(report):
    if all(report[i] < report[i+1] and abs(report[i] - report[i+1]) <= 3 for i in range(len(report) -1)):
        return True
    if all(report[i] > report[i+1] and abs(report[i] - report[i+1]) <= 3 for i in range(len(report) -1)):
        return True
    return False

with open("input", "r") as input:
    res = 0;
    possibleSafe = []
    for line in input.readlines():
        line = line.removesuffix('\n')
        report = list(map(int, line.split(' ')))
        if isReportSafe(report):
            res += 1
        else:
            possibleSafe.append(report)

    print(f"Part1 response: {res}")
#part2
    for report in possibleSafe:
        for i in range(len(report)):
            copy = report.copy()
            copy.pop(i)
            if isReportSafe(copy):
                res +=1
                break


    print(f"Part2 response: {res}")
