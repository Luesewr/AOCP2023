f = open("inputs/day18.txt")
dig_plan = [instruction.split(" ") for instruction in f.read().split("\n")]
points = []
circumference = 0
x = 0
y = 0


def area(p):
    return abs(sum(x0*y1 - x1*y0 for ((x0, y0), (x1, y1)) in segments(p))) // 2


def segments(p):
    return zip(p, p[1:] + [p[0]])


for instruction_index, instruction in enumerate(dig_plan):
    direction, len_str, color = instruction
    length = int(color[2:-2], 16)
    d = color[-2]
    points.append((x, y))
    circumference += length

    if d == '0':
        x += length
    elif d == '1':
        y += length
    elif d == '2':
        x -= length
    elif d == '3':
        y -= length

print(area(points) + circumference // 2 + 1)
