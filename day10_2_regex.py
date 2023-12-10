import regex as re

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
    if direction == 0:
        return x, y - 1
    elif direction == 1:
        return x + 1, y
    elif direction == 2:
        return x, y + 1
    elif direction == 3:
        return x - 1, y
    else:
        raise Exception("Invalid direction")


current_search = []
start_direction = -1
for i in range(4):
    new_location = apply_direction(start_x, start_y, i)
    new_x, new_y = new_location
    if not check_bounds(new_x, new_y, width, height) or ((i + 2) % 4) not in accepted_directions[lines[new_y][new_x]]:
        continue
    current_search.append((new_location, (start_x, start_y), 1))
    start_direction = i
    break

loop_positions = set()
while len(current_search) > 0:
    current_element = current_search.pop(0)
    current_position, current_origin, distance = current_element
    current_x, current_y = current_position
    origin_x, origin_y = current_origin
    current_accepted_directions = accepted_directions[lines[current_y][current_x]]

    loop_positions.add(current_position)

    if current_x == start_x and current_y == start_y:
        direction = -1
        if current_y == origin_y - 1:
            direction = 2
        elif current_x == origin_x + 1:
            direction = 3
        elif current_y == origin_y + 1:
            direction = 0
        elif current_x == origin_x - 1:
            direction = 1
        piece = [['#', 'L', '|', 'J'], ['L', '#', 'F', '-'], ['|', 'F', '#', '7'], ['J', '-', '7', '#']]
        line = list(lines[start_y])
        line[start_x] = piece[direction][start_direction]
        lines[start_y] = "".join(line)
        break

    for i in range(4):
        new_location = apply_direction(current_x, current_y, i)
        new_x, new_y = new_location
        if (not check_bounds(new_x, new_y, width, height)) or (new_location == current_origin) or (i not in current_accepted_directions) or (((i + 2) % 4) not in accepted_directions[lines[new_y][new_x]]):
            continue
        current_search.append((new_location, current_position, distance + 1))
        break

t = 0

for y in range(height):
    for x in range(width):
        if (x, y) not in loop_positions:
            line = list(lines[y])
            line[x] = '.'
            lines[y] = "".join(line)

    line = lines[y]

    line = re.sub(r'(F(-)*7)|(L(-)*J)', '', line)
    line = re.sub(r'(F(-)*J)|(L(-)*7)', '|', line)
    line = re.sub(r'\|\|', '', line)
    matches = re.search(r'\|\.+\|', line)
    if matches is not None:
        t += sum([len(match) - 2 for match in matches.captures()])

print(t)
