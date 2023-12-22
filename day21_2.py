# 452736719465550 too low
# 626078181213049 too high
# 624686714474832 not right
# 626075086420000 not right
# 626076711706062 not right
# 626078993855994 not right
# 624687527117777 not right

f = open("inputs/other_day21.txt")
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


def count_pots(x, y, steps, bounded, positions=None):
    if steps <= 0:
        return 0
    if positions is None:
        positions = {(x, y)}
    for _ in range(steps):
        new_positions = set()

        for x, y in positions:
            for d in range(4):
                new_x, new_y = apply_direction(x, y, d)
                if lines[(new_y + length) % length][(new_x + length) % length] != '#':
                    if not bounded:
                        new_positions.add((new_x, new_y))
                    elif check_bounds(new_x, new_y, length, length):
                        new_positions.add((new_x, new_y))

        positions = new_positions
    # print(positions)
    return positions


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
remaining_steps = steps_needed % length
print(remaining_steps)


if steps_needed % 2 == 1:
    t += len(even_positions) * (((lengths_covered - 1) // 2) ** 2)
    t += len(odd_positions) * (((lengths_covered - 1) // 2 - 1) ** 2)
    small_edges = count_pots(start_x, start_y, length + remaining_steps, False)
    big_edges = count_pots(start_x, start_y, 2 * length + remaining_steps, False)
else:
    t += len(odd_positions) * (((lengths_covered - 1) // 2) ** 2)
    t += len(even_positions) * (((lengths_covered - 1) // 2 - 1) ** 2)
    small_edges = count_pots(start_x, start_y, length + remaining_steps, False)
    big_edges = count_pots(start_x, start_y, 2 * length + remaining_steps, False)

small_edges = list(filter(lambda x: ((x[0] < 0 or x[0] >= length) and (x[1] < 0 or x[1] >= length)), small_edges))
big_edges = list(filter(lambda x: (((0 > x[0] > -length) or (length <= x[0] < 2 * length)) and ((0 > x[1] > -length) or (length <= x[1] < 2 * length))), big_edges))
print(t)
t += len(small_edges) * ((lengths_covered - 1) // 2 + 1)
t += len(big_edges) * ((lengths_covered - 1) // 2)
print(t)

corners = list(filter(lambda x: ((x[0] < 0 or x[0] >= length) and (0 <= x[1] < length)) or ((x[1] < 0 or x[1] >= length) and (0 <= x[0] < length)), count_pots(start_x, start_y, length + remaining_steps, False)))

t += len(corners)
print(t)
