import heapq

f = open("inputs/day17.txt")
lines = f.read().split("\n")
heat_values = [[int(i) for i in line] for line in lines]
height = len(heat_values)
width = len(heat_values[0])


class QueueItem:
    def __init__(self, location, heat_loss, straight_counter):
        self.location = location
        self.heat_loss = heat_loss
        self.straight_counter = straight_counter

    def __lt__(self, other):
        return self.heat_loss - self.location[0] - self.location[1] < other.heat_loss - other.location[0] - other.location[1]


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


heap = []
heapq.heappush(heap, QueueItem((1, 0, 0), heat_values[0][1], 1))
heapq.heappush(heap, QueueItem((0, 1, 1), heat_values[1][0], 1))

best_value = sum([sum(values) for values in heat_values])

visited = set()

while heap:
    pq_item = heapq.heappop(heap)
    x, y, d = pq_item.location
    info = (x, y, d, pq_item.straight_counter)
    if info in visited:
        continue

    visited.add(info)

    if x == width - 1 and y == height - 1 and pq_item.straight_counter >= 4:
        best_value = pq_item.heat_loss
        break

    for i in range(-1, 2):
        if i == 0 and pq_item.straight_counter >= 10:
            continue
        if i != 0 and pq_item.straight_counter < 4:
            continue
        direction = (d + i + 4) % 4
        new_x, new_y = apply_direction(x, y, direction)
        new_straight_counter = pq_item.straight_counter * (i == 0) + 1
        new_info = (new_x, new_y, direction, new_straight_counter)
        if new_info not in visited and check_bounds(new_x, new_y, width, height):
            heapq.heappush(heap, QueueItem((new_x, new_y, direction), pq_item.heat_loss + heat_values[new_y][new_x], new_straight_counter))

print(best_value)
