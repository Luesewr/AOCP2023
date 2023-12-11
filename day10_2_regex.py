import re

f = open("inputs/day10.txt")
lines = f.read().split("\n")
start_y = list(map(lambda line: "S" in line, lines)).index(True)
start_x = lines[start_y].index("S")
width = len(lines[start_y])
height = len(lines)

accepted_directions = {
    '|': [0, 2],
    '-': [1, 3],
    'L': [0, 1],
    'J': [0, 3],
    '7': [2, 3],
    'F': [1, 2],
    '.': [],
    'S': [0, 1, 2, 3],
}


def check_bounds(x, y, width, height):
    return 0 <= x <= width - 1 and 0 <= y <= height - 1


def apply_direction(x, y, direction):
    applied_directions = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
    return applied_directions[direction]


current_search = None
start_directions = []
for i in range(4):
    new_location = apply_direction(start_x, start_y, i)
    new_x, new_y = new_location
    if not check_bounds(new_x, new_y, width, height) or ((i + 2) % 4) not in accepted_directions[lines[new_y][new_x]]:
        continue
    current_search = (new_location, (start_x, start_y), 1)
    start_directions.append(i)

piece = [['#', 'L', '|', 'J'], ['L', '#', 'F', '-'], ['|', 'F', '#', '7'], ['J', '-', '7', '#']]

line = list(lines[start_y])
line[start_x] = piece[start_directions[0]][start_directions[1]]
lines[start_y] = "".join(line)

loop_positions = set()
while len(current_search) > 0:
    current_element = current_search
    current_position, current_origin, distance = current_element
    current_x, current_y = current_position
    origin_x, origin_y = current_origin
    current_accepted_directions = accepted_directions[lines[current_y][current_x]]

    loop_positions.add(current_position)

    if current_x == start_x and current_y == start_y:
        break

    for i in range(4):
        new_location = apply_direction(current_x, current_y, i)
        new_x, new_y = new_location
        if (not check_bounds(new_x, new_y, width, height)) or (new_location == current_origin) or (i not in current_accepted_directions) or (((i + 2) % 4) not in accepted_directions[lines[new_y][new_x]]):
            continue
        current_search = (new_location, current_position, distance + 1)
        break

lines = ["".join([character if (x, y) in loop_positions else "." for x, character in enumerate(line)]) for y, line in enumerate(lines)]
matches = re.findall(r'(?:\||F-*J|L-*7)(?:\.|F-*7|L-*J)*(?:\||F-*J|L-*7)', "\n".join(lines))
print(sum([match.count('.') for match in matches]))
