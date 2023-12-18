import re

f = open("inputs/day18.txt")
dig_plan = [instruction.split(" ") for instruction in f.read().split("\n")]
dig_map = [['.']]
x = 0
y = 0
x_offset = 0
y_offset = 0
t = 0
piece = [['#', 'L', '|', 'J'], ['L', '#', 'F', '-'], ['|', 'F', '#', '7'], ['J', '-', '7', '#']]
d_to_int = {'U': 0, 'R': 1, 'D': 2, 'L': 3}

for instruction_index, instruction in enumerate(dig_plan):
    d, len_str, color = instruction
    length = int(len_str)
    t += length
    next_d = dig_plan[(instruction_index + 1) % len(dig_plan)][0]

    for i in range(length):
        if d == 'R':
            x += 1
        elif d == 'D':
            y += 1
        elif d == 'L':
            x -= 1
        elif d == 'U':
            y -= 1

        if x + x_offset < 0:
            dig_map = [['.', *line] for line in dig_map]
            x_offset += 1
        if y + y_offset < 0:
            dig_map = [[], *dig_map]
            y_offset += 1
        if y + y_offset == len(dig_map):
            dig_map.append(['.' for _ in range(x + x_offset + 1)])
        elif x + x_offset >= len(dig_map[y + y_offset]):
            dig_map[y + y_offset].extend(['.' for _ in range(x + x_offset - len(dig_map[y + y_offset]) + 1)])

        if i == length - 1:
            dig_map[y + y_offset][x + x_offset] = piece[(d_to_int[d] + 2) % 4][d_to_int[next_d]]
        elif d == 'R' or d == 'L':
            dig_map[y + y_offset][x + x_offset] = '-'
        elif d == 'U' or d == 'D':
            dig_map[y + y_offset][x + x_offset] = '|'

string_map = '\n'.join([''.join(line) for line in dig_map])
matches = re.findall(r'(?:\||F-*J|L-*7)(?:\.|F-*7|L-*J)*(?:\||F-*J|L-*7)', string_map)
t += sum([match.count('.') for match in matches])

print(t)
