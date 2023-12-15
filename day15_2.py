import re

f = open("inputs/day15.txt")
operations = list(map(lambda x: re.split(r"[-=]", x), f.read().split(",")))

boxes = [{} for _ in range(256)]

for index, (lens_hash, value_string) in enumerate(operations):
    box_index = 0
    for c in lens_hash:
        box_index += ord(c)
        box_index *= 17
        box_index %= 256

    if len(value_string) == 0:
        if lens_hash in boxes[box_index]:
            boxes[box_index].pop(lens_hash)
    else:
        value = int(value_string)
        if lens_hash in boxes[box_index]:
            boxes[box_index][lens_hash] = (value, boxes[box_index][lens_hash][1])
        else:
            boxes[box_index][lens_hash] = (value, index)

t = 0

for box_index, box in enumerate(boxes):
    box_values = sorted(box.values(), key=lambda x: x[1])
    for i in range(len(box_values)):
        t += (box_index + 1) * (i + 1) * (box_values[i][0])

print(t)
