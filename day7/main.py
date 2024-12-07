
def sum1(i,numbers, value, sum):
    if sum == value and i == len(numbers):
        return True
    if sum > value:
        return False
    if len(numbers) == i:
        return False

    concatenation = int(str(sum) + str(numbers[i]))
    print(sum, numbers[i], concatenation)
    return (
        sum1(i+1, numbers, value, sum + numbers[i])
        or sum1(i+1, numbers, value, sum * numbers[i])
        or sum1(i+1, numbers, value, concatenation)
    )

with open("input", "r") as file:
    lines = [line.removesuffix("\n") for line in file.readlines()]

    equations = [line.split(":") for line in lines]

    res = 0
    for equation in equations:
        value = int(equation[0])
        numbers = [int(x) for x in equation[1].lstrip().split(" ")]

        if sum1(1, numbers, value, numbers[0]):
            res += value
    print(res)
