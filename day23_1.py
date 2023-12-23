f = open("inputs/day23.txt")
rows = f.read().split('\n')
start_y = 0
start_x = rows[start_y].index('.')
end_y = len(rows) - 1
end_x = rows[end_y].index('.')
direction_lookup = {'^': 0, '>': 1, 'v': 2, '<': 3}


def apply_direction(x, y, direction):
    if direction == 0:
        return x, y - 1
    elif direction == 1:
        return x + 1, y
    elif direction == 2:
        return x, y + 1
    elif direction == 3:
        return x - 1, y


stack = [(start_x, start_y + 1, 1, {(start_x, start_y)})]

longest_depth = 0

while len(stack) > 0:
    x, y, depth, visited = stack.pop()

    if x == end_x and y == end_y:
        if depth > longest_depth:
            longest_depth = depth
        continue

    new_visited = visited.copy()
    new_visited.add((x, y))

    if rows[y][x] != '.':
        d = direction_lookup[rows[y][x]]
        new_x, new_y = apply_direction(x, y, d)
        if rows[new_y][new_x] != '#' and (new_x, new_y) not in visited:
            stack.append((new_x, new_y, depth + 1, new_visited))
    else:
        for d in range(4):
            new_x, new_y = apply_direction(x, y, d)
            if rows[new_y][new_x] != '#' and (new_x, new_y) not in visited:
                stack.append((new_x, new_y, depth + 1, new_visited))

print(longest_depth)
