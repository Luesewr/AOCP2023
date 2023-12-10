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


def flood_fill(position, exclude, dest):
    if position in dest:
        return True
    queue = [position]
    while len(queue) > 0:
        current_element = queue.pop(0)
        current_x, current_y = current_element
        if current_element in dest or current_element in exclude:
            continue
        if not check_bounds(current_x, current_y, width, height):
            return False
        dest.add(current_element)
        for direction in range(4):
            queue.append(apply_direction(current_x, current_y, direction))
    return True


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

found_furthest = False
loop_visits = []
loop_positions = set()
while len(current_search) > 0:
    current_element = current_search.pop(0)
    current_position, current_origin, distance = current_element
    current_x, current_y = current_position
    origin_x, origin_y = current_origin
    current_accepted_directions = accepted_directions[lines[current_y][current_x]]

    direction = -1
    if current_y == origin_y - 1:
        direction = 0
    elif current_x == origin_x + 1:
        direction = 1
    elif current_y == origin_y + 1:
        direction = 2
    elif current_x == origin_x - 1:
        direction = 3

    loop_positions.add(current_position)

    if current_x == start_x and current_y == start_y:
        loop_visits.append((*current_position, [start_direction, direction]))
        break

    for i in range(4):
        new_location = apply_direction(current_x, current_y, i)
        new_x, new_y = new_location
        if (not check_bounds(new_x, new_y, width, height)) or (new_location == current_origin) or (i not in current_accepted_directions) or (((i + 2) % 4) not in accepted_directions[lines[new_y][new_x]]):
            continue
        current_search.append((new_location, current_position, distance + 1))
        loop_visits.append((*current_position, [direction, i]))
        break

left_area = set()
right_area = set()
left_valid = True
right_valid = True

for x, y, directions in loop_visits:
    for direction in directions:
        if left_valid:
            left_valid = flood_fill(apply_direction(x, y, (direction + 3) % 4), loop_positions, left_area)
        if right_valid:
            right_valid = flood_fill(apply_direction(x, y, (direction + 1) % 4), loop_positions, right_area)

if left_valid:
    print(len(left_area))
if right_valid:
    print(len(right_area))
