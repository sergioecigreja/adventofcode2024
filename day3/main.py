import re

with open("input", "r") as input:
    text = input.read()
    occurrences = re.findall(r"mul\(\s*\d+\s*,\s*\d+\s*\)", text)
    res = 0
    for occurrence in occurrences:
        numbers = re.findall(r"\d+", occurrence)
        res += int(numbers[0]) * int(numbers[1])

    print(res)

    matches = re.findall(r'don\'t\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\)', text)
    enabled = True
    res = 0
    for match in matches:
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        elif enabled:
            numbers = re.findall(r"\d+", match)
            res += int(numbers[0]) * int(numbers[1])
    print(res)

#161289189
#629175469
#47919500 too low
#res += [int(a) * int(b) for a, b in [re.findall(r'\d{1,3}', match)]][0] more pythonic
