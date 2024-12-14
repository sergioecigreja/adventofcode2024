import re

class Button:
    def __init__(self, type: str, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.type = type

    def __str__(self):
        return f"Button {self.type} X-{self.x} Y-{self.y}"

class Prize:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.y = y

    def __str__(self):
        return f"Prize X-{self.x} Y-{self.y}"

class Arcade:
    def __init__(self, a: Button, b: Button, prize: Prize):
        self.a = a
        self.b = b
        self.prize = prize

    def valid(self, x,y) -> bool:
        max_inc_x = max(self.a.x, self.b.x)
        max_inc_y = max(self.a.y, self.b.y)

        if max_inc_x * 100 + x < self.prize.x or max_inc_y * 100 + y < self.prize.y:
            return False
        return True

    def __str__(self):
        return f"Arcade {self.a} | {self.b}"

    def __repr__(self):
        return f"Arcade {self.a} | {self.b}"

    def __iter__(self):
            yield self.a
            yield self.b
            yield self.prize

def to_arcade(arr):
    pattern_button = r"Button (\w): X\+(\d+), Y\+(\d+)"
    pattern_prize = r"Prize: X=(\d+), Y=(\d+)"

    matcha = re.match(pattern_button, arr[0])
    matchb = re.match(pattern_button, arr[1])
    matchp = re.match(pattern_prize, arr[2])
    if (matcha and matchb and matchp):
        btna = Button(matcha.group(1), int(matcha.group(2)), int(matcha.group(3)))
        btnb = Button(matchb.group(1), int(matchb.group(2)), int(matchb.group(3)))
        prize = Prize(int(matchp.group(1)), int(matchp.group(2)))
        return Arcade(btna, btnb, prize)

with open("input", "r") as file:
    lines = [x.removesuffix("\n") for x in filter(lambda l: l != "\n", file.readlines())]
    arcadelines = [lines[i:i+3] for i in range(0, len(lines), 3)]

    patternButton = r"Button (\w): X\+(\d+), Y\+(\d+)"
    patternPrize = r"Prize: X=(\d+), Y=(\d+)"
    arcades = []
    for arcadeline in arcadelines:
        arcades.append(to_arcade(arcadeline))

    res = 0
    for arcade in arcades:
        b = ((arcade.a.y * arcade.prize.x) - (arcade.a.x * arcade.prize.y)) / ((arcade.a.y * arcade.b.x) - (arcade.a.x * arcade.b.y))
        if b == int(b):
            a = (arcade.prize.y - (arcade.b.y * b)) / arcade.a.y
            res += a * 3 + b
    print(res)

    #part2
    res2 = 0
    for arcade in arcades:
        arcade.prize = Prize(arcade.prize.x + 10000000000000, arcade.prize.y + 10000000000000)
        b = ((arcade.a.y * arcade.prize.x) - (arcade.a.x * arcade.prize.y)) / ((arcade.a.y * arcade.b.x) - (arcade.a.x * arcade.b.y))
        if b == int(b):
            a = (arcade.prize.y - (arcade.b.y * b)) / arcade.a.y
            res2 += a * 3 + b
    print(res2)
