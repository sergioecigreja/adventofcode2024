import re
import uuid


class Robot:
    def __init__(self,x, y, vx, vy):
        self.id = uuid.uuid4()
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def __str__(self):
        return f"x:{self.x} | y:{self.y} | vx:{self.vx} | vy:{self.vy}"
    def __repr__(self):
        return f"x:{self.x} | y:{self.y} | vx:{self.vx} | vy:{self.vy}"

def display(robots, width, height,step, file):

    for y in range(height):
        row = []

        for x in range(width):
            # Check if any robot is at position (x, y)
            val = 'x' if any(r.x == x and r.y == y for r in robots) else '.'
            row.append(val)

        file.write(''.join(row))
        file.write("\n")


    file.write(str(step))
    file.write("\n")

with open("input", "r") as file:
    lines = [x.removesuffix("\n") for x in file.readlines()]
    width = 101
    height = 103
    time = 100

    robots = []
    for line in lines:
        pattern = r"-?\d+"
        numbers = re.findall(pattern, line)
        numbers = list(map(int, numbers))
        robots.append(Robot(numbers[0], numbers[1], numbers[2], numbers[3]))

    for robot in robots:
        robot.x = (robot.x + robot.vx * time)%width
        robot.y = (robot.y + robot.vy * time)%height

    tl,tr,bl,br = 0,0,0,0

    for robot in robots:
        #tl 0 - width-1/2 | 0 - height-1/2
        if 0 <= robot.x < (width-1)/2 and 0 <= robot.y < (height-1)/2:
            tl += 1
        #tr 0 - width-1/2 | 0 - height-1/2
        if (width-1)/2 < robot.x < width and 0 <= robot.y < (height-1)/2:
            tr += 1
        #bl 0 width-1/2 | height-1/2 height
        if 0 <= robot.x < (width-1)/2 and (height-1)/2 < robot.y < height:
            bl += 1
        #br width-1/2 width | height-1/2 height
        if (width-1)/2 < robot.x < width and (height-1)/2 < robot.y < height:
            br += 1

    print(tl,tr,bl,br)

    #part2
    res2 = 1
    robots = []
    for line in lines:
        pattern = r"-?\d+"
        numbers = re.findall(pattern, line)
        numbers = list(map(int, numbers))
        robots.append(Robot(numbers[0], numbers[1], numbers[2], numbers[3]))


    bl = 0
    br = 0
    res2 = 1
    with open("output", "w") as f:
        while res2 <= 10000:
            s = set([])
            for robot in robots:
                robot.x = (robot.x + robot.vx * res2)%width
                robot.y = (robot.y + robot.vy * res2)%height
                s.add((robot.x, robot.y))

            #Better to use Chinese Remainder Theorem, or to use statistics to search for robot density
            if len(s) == len(robots):
                break
        display(robots, width, height, res2, f)
