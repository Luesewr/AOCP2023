# 452736719465550 too low
# 626078181213049 too high
# 624686714474832 not right
# 626075086420000 not right
# 626076711706062 not right
# 626078993855994 not right
# 624687527117777 not right

f = open("inputs/day21.txt")
lines = f.read().split('\n')
start_y = ['S' in line for line in lines].index(True)
start_x = lines[start_y].index('S')
length = len(lines)
steps_needed = 26501365

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


def count_pots(x, y, steps):
    if steps <= 0:
        return 0
    positions = {(x, y)}
    for _ in range(steps):
        new_positions = set()

        for x, y in positions:
            for d in range(4):
                new_x, new_y = apply_direction(x, y, d)
                if check_bounds(new_x, new_y, length, length) and lines[new_y][new_x] != '#':
                    new_positions.add((new_x, new_y))

        positions = new_positions
    # print(positions)
    return len(positions)


prev_positions = None
prev_prev_positions = None

even_positions = None
odd_positions = None
steps = 0
while True:
    steps += 1
    new_positions = set()

    for x, y in current_positions:
        for d in range(4):
            new_x, new_y = apply_direction(x, y, d)
            if check_bounds(new_x, new_y, length, length) and lines[new_y][new_x] != '#':
                new_positions.add((new_x, new_y))

    if new_positions == prev_positions and current_positions == prev_prev_positions:
        if steps % 2 == 0:
            even_positions = new_positions
            odd_positions = current_positions
        else:
            odd_positions = new_positions
            even_positions = current_positions
        break
    prev_prev_positions = prev_positions
    prev_positions = current_positions
    current_positions = new_positions


t = 0
lengths_covered = ((steps_needed + 1) - (length - 1) // 2) // length * 2 + 1
print(lengths_covered)
full_layouts_covered = (lengths_covered * lengths_covered + 1) // 2
print(full_layouts_covered)

t += len(even_positions) * full_layouts_covered

print(t)
# remaining_steps = (steps_needed - ((lengths_covered - 1) // 2 * length) - 1)
remaining_steps = steps_needed % length
print(remaining_steps)
half_length_index = (length - 1) // 2

side_pots_starting_positions = [(half_length_index, 0), (length - 1, half_length_index), (half_length_index, length - 1), (0, half_length_index)]
side_pots_sizes = [count_pots(x, y, remaining_steps) for x, y in side_pots_starting_positions]
print(side_pots_sizes)

corner_pots_starting_positions = [(0, 0), (length - 1, 0), (length - 1, length - 1), (0, length - 1)]
corner_pots_sizes = [count_pots(x, y, remaining_steps) for x, y in corner_pots_starting_positions]
print(corner_pots_sizes)

t += sum(side_pots_sizes)
t += sum(corner_pots_sizes) * ((lengths_covered - 1) // 2 - 1)

print(t)
