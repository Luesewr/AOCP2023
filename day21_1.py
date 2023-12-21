f = open("inputs/day21.txt")
lines = f.read().split('\n')
start_y = ['S' in line for line in lines].index(True)
start_x = lines[start_y].index('S')
width = len(lines[start_y])
height = len(lines)

current_positions = {(start_x, start_y)}


def apply_direction(x, y, direction):
    if direction == 0:
        return x, y - 1
    elif direction == 1:
        return x + 1, y
    elif direction == 2:
        return x, y + 1
    elif direction == 3:
        return x - 1, y


def check_bounds(x, y, width, height):
    return 0 <= x <= width - 1 and 0 <= y <= height - 1


for _ in range(64):
    new_positions = set()

    for x, y in current_positions:
        for d in range(4):
            new_x, new_y = apply_direction(x, y, d)
            if check_bounds(new_x, new_y, width, height) and lines[new_y][new_x] != '#':
                new_positions.add((new_x, new_y))

    current_positions = new_positions

print(len(current_positions))
