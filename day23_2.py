import heapq

f = open("inputs/day23.txt")
rows = f.read().split('\n')
start_y = 0
start_x = rows[start_y].index('.')
end_y = len(rows) - 1
end_x = rows[end_y].index('.')
height = len(rows)
width = len(rows[start_y])


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbours = []

    def __repr__(self):
        return f'Node({self.x}, {self.y})'


class QueueNode:
    def __init__(self, node, depth, visited):
        self.node = node
        self.depth = depth
        self.visited = visited

    def __lt__(self, other):
        return other.depth - (self.node.x + self.node.y) < self.depth - (other.node.x + other.node.y)


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


starting_node = Node(start_x, start_y)
ending_node = Node(end_x, end_y)
nodes = {(start_x, start_y): starting_node, (end_x, end_y): ending_node}

for x in range(1, width - 1):
    for y in range(1, height - 1):
        connections = 0
        if rows[y][x] != '#':
            for d in range(4):
                new_x, new_y = apply_direction(x, y, d)
                if rows[new_y][new_x] != '#':
                    connections += 1
            if connections > 2:
                nodes[(x, y)] = Node(x, y)

for pos, node in nodes.items():
    stack = [(node.x, node.y, 0, set())]

    while len(stack) > 0:
        x, y, depth, visited = stack.pop()
        if (x, y) in nodes and (x, y) != pos:
            node.neighbours.append((nodes[(x, y)], depth))
            continue
        new_visited = visited.copy()
        new_visited.add((x, y))
        for d in range(4):
            new_x, new_y = apply_direction(x, y, d)
            if check_bounds(new_x, new_y, width, height) and rows[new_y][new_x] != '#' and (new_x, new_y) not in visited:
                stack.append((new_x, new_y, depth + 1, new_visited))

heap = [QueueNode(starting_node, 0, set())]

longest_depth = 0
ends_between_best = 0

while len(heap) > 0:
    queue_node = heapq.heappop(heap)
    node = queue_node.node
    depth = queue_node.depth
    visited = queue_node.visited

    if node == ending_node:
        ends_between_best += 1
        if depth > longest_depth:
            longest_depth = depth
            ends_between_best = 0
        if ends_between_best > longest_depth:
            break
        continue

    new_visited = visited.copy()
    new_visited.add(node)

    for neighbour, neighbour_depth in node.neighbours:
        if neighbour not in visited:
            heapq.heappush(heap, QueueNode(neighbour, depth + neighbour_depth, new_visited))

print(longest_depth)
