f = open("inputs/day16.txt")
lines = f.read().split('\n')
height = len(lines)
width = len(lines[0])
direction_map = {
    0: {'-': [(1, 0, 0)], '/': [(0, -1, 3)], '\\': [(0, 1, 1)], '|': [(0, -1, 3), (0, 1, 1)], '.': [(1, 0, 0)]},
    1: {'-': [(-1, 0, 1), (1, 0, 3)], '/': [(-1, 0, 1)], '\\': [(1, 0, 3)], '|': [(0, 1, 0)], '.': [(0, 1, 0)]},
    2: {'-': [(-1, 0, 0)], '/': [(0, 1, 3)], '\\': [(0, -1, 1)], '|': [(0, -1, 1), (0, 1, 3)], '.': [(-1, 0, 0)]},
    3: {'-': [(-1, 0, 3), (1, 0, 1)], '/': [(1, 0, 1)], '\\': [(-1, 0, 3)], '|': [(0, -1, 0)], '.': [(0, -1, 0)]},
}


def calculate_energized(start_x, start_y, start_d):
    location_stack = [(start_x, start_y, start_d)]
    visited_locations = set()
    energized_tiles = set()

    while len(location_stack) > 0:
        x, y, d = location_stack.pop()
        if (x, y, d) in visited_locations:
            continue
        visited_locations.add((x, y, d))
        energized_tiles.add((x, y))

        for new_location in direction_map[d][lines[y][x]]:
            new_pos_x = x + new_location[0]
            new_pos_y = y + new_location[1]
            new_pos_d = (d + new_location[2]) % 4
            if 0 <= new_pos_x < width and 0 <= new_pos_y < height:
                location_stack.append((new_pos_x, new_pos_y, new_pos_d))

    return len(energized_tiles)


most_energized = 0

for i in range(height):
    most_energized = max(most_energized, calculate_energized(0, i, 0))
    most_energized = max(most_energized, calculate_energized(width - 1, i, 2))

for i in range(1, width - 1):
    most_energized = max(most_energized, calculate_energized(i, 0, 1))
    most_energized = max(most_energized, calculate_energized(i, height - 1, 3))

print(most_energized)
