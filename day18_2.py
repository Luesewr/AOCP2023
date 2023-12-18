from shapely import Polygon

f = open("inputs/day18.txt")
dig_plan = [instruction.split(" ") for instruction in f.read().split("\n")]
points = []
circumference = 0
x = 0
y = 0
t = 0

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

t += int(Polygon(points).area) + circumference // 2 + 1

print(t)
