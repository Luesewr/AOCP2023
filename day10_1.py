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

current_search = [((start_x, start_y), (start_x, start_y), 0)]

while len(current_search) > 0:
    current_element = current_search.pop(0)
    current_position, current_origin, distance = current_element
    current_x, current_y = current_position
    origin_x, origin_y = current_origin
    current_accepted_directions = accepted_directions[lines[current_y][current_x]]

    if len(current_search) > 0 and current_search[0][2] == distance and current_search[0][0] == current_position:
        print(distance)
        break

    if current_y > 0 and current_y - 1 != origin_y and 0 in current_accepted_directions and 2 in accepted_directions[lines[current_y - 1][current_x]]:
        current_search.append(((current_x, current_y - 1), (current_x, current_y), distance + 1))
    if current_x < width - 1 and current_x + 1 != origin_x and 1 in current_accepted_directions and 3 in accepted_directions[lines[current_y][current_x + 1]]:
        current_search.append(((current_x + 1, current_y), (current_x, current_y), distance + 1))
    if current_y < height - 1 and current_y + 1 != origin_y and 2 in current_accepted_directions and 0 in accepted_directions[lines[current_y + 1][current_x]]:
        current_search.append(((current_x, current_y + 1), (current_x, current_y), distance + 1))
    if current_x > 0 and current_x - 1 != origin_x and 3 in current_accepted_directions and 1 in accepted_directions[lines[current_y][current_x - 1]]:
        current_search.append(((current_x - 1, current_y), (current_x, current_y), distance + 1))
