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

current_search = []
start_direction = -1
if start_y > 0 and 2 in accepted_directions[lines[start_y - 1][start_x]]:
    current_search.append(((start_x, start_y - 1), (start_x, start_y), 1))
    start_direction = 0
elif start_x < width - 1 and 3 in accepted_directions[lines[start_y][start_x + 1]]:
    current_search.append(((start_x + 1, start_y), (start_x, start_y), 1))
    start_direction = 1
elif start_y < height - 1 and 0 in accepted_directions[lines[start_y + 1][start_x]]:
    current_search.append(((start_x, start_y + 1), (start_x, start_y), 1))
    start_direction = 2
elif start_x > 0 and 1 in accepted_directions[lines[start_y][start_x - 1]]:
    current_search.append(((start_x - 1, start_y), (start_x, start_y), 1))
    start_direction = 3

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

    secondary_direction = -1

    if current_y > 0 and current_y - 1 != origin_y and 0 in current_accepted_directions and 2 in accepted_directions[lines[current_y - 1][current_x]]:
        current_search.append(((current_x, current_y - 1), (current_x, current_y), distance + 1))
        secondary_direction = 0
    if current_x < width - 1 and current_x + 1 != origin_x and 1 in current_accepted_directions and 3 in accepted_directions[lines[current_y][current_x + 1]]:
        current_search.append(((current_x + 1, current_y), (current_x, current_y), distance + 1))
        secondary_direction = 1
    if current_y < height - 1 and current_y + 1 != origin_y and 2 in current_accepted_directions and 0 in accepted_directions[lines[current_y + 1][current_x]]:
        current_search.append(((current_x, current_y + 1), (current_x, current_y), distance + 1))
        secondary_direction = 2
    if current_x > 0 and current_x - 1 != origin_x and 3 in current_accepted_directions and 1 in accepted_directions[lines[current_y][current_x - 1]]:
        current_search.append(((current_x - 1, current_y), (current_x, current_y), distance + 1))
        secondary_direction = 3

    loop_visits.append((*current_position, [direction, secondary_direction]))


def flood_fill(x, y, exclude, dest):
    if (x, y) in dest:
        return True
    queue = [(x, y)]
    while len(queue) > 0:
        current_element = queue.pop(0)
        current_x, current_y = current_element
        if current_element in dest or current_element in exclude:
            continue
        if current_x <= 0 or current_y <= 0 or current_x >= width - 1 or current_y >= height - 1:
            return False
        dest.add(current_element)
        if current_y > 0:
            queue.append((current_x, current_y - 1))
        if current_x < width - 1:
            queue.append((current_x + 1, current_y))
        if current_y < height - 1:
            queue.append((current_x, current_y + 1))
        if current_x > 0:
            queue.append((current_x - 1, current_y))
    return True


left_area = set()
right_area = set()
left_valid = True
right_valid = True

for x, y, directions in loop_visits:
    for direction in directions:
        if left_valid:
            if direction == 0:
                left_valid = flood_fill(x - 1, y, loop_positions, left_area)
            elif direction == 1:
                left_valid = flood_fill(x, y - 1, loop_positions, left_area)
            elif direction == 2:
                left_valid = flood_fill(x + 1, y, loop_positions, left_area)
            elif direction == 3:
                left_valid = flood_fill(x, y + 1, loop_positions, left_area)

        if right_valid:
            if direction == 0:
                right_valid = flood_fill(x + 1, y, loop_positions, right_area)
            elif direction == 1:
                right_valid = flood_fill(x, y + 1, loop_positions, right_area)
            elif direction == 2:
                right_valid = flood_fill(x - 1, y, loop_positions, right_area)
            elif direction == 3:
                right_valid = flood_fill(x, y - 1, loop_positions, right_area)

if left_valid:
    print(len(left_area))
if right_valid:
    print(len(right_area))
