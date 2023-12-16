from queue import Queue

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


def apply_direction(x, y, d):
    if d == 0:
        return x + 1, y
    if d == 1:
        return x, y + 1
    if d == 2:
        return x - 1, y
    if d == 3:
        return x, y - 1


def check_bounds(x, y, width, height):
    return 0 <= x < width and 0 <= y < height


def calculate_energized(start_x, start_y, start_d):
    location_queue = Queue()
    location_queue.put((start_x, start_y, start_d))
    visited_locations = set()
    energized_tiles = set()

    while not location_queue.empty():
        x, y, d = location_queue.get()
        if (x, y, d) in visited_locations:
            continue
        visited_locations.add((x, y, d))
        energized_tiles.add((x, y))

        for new_location in direction_map[d][lines[y][x]]:
            new_pos_x = x + new_location[0]
            new_pos_y = y + new_location[1]
            new_pos_d = (d + new_location[2]) % 4
            if check_bounds(new_pos_x, new_pos_y, width, height):
                location_queue.put((new_pos_x, new_pos_y, new_pos_d))

    return len(energized_tiles)


most_energized = 0

for i in range(height):
    most_energized = max(most_energized, calculate_energized(0, i, 0))
    most_energized = max(most_energized, calculate_energized(width - 1, i, 2))

for i in range(1, width - 1):
    most_energized = max(most_energized, calculate_energized(i, 0, 1))
    most_energized = max(most_energized, calculate_energized(i, height - 1, 3))

print(most_energized)
