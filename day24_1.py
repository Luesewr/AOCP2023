import re
from itertools import combinations

f = open("inputs/day24.txt")
lines = [re.sub(r' +', ' ', line).split(' @ ') for line in f.read().split('\n')]
data = [(line[0].split(', '), line[1].split(', ')) for line in lines]
data = [([int(i) for i in pos], [int(i) for i in vel]) for pos, vel in data]

test_area_min = 200000000000000
test_area_max = 400000000000000
intersections_in_test_area = 0

combinations = list(combinations(data, 2))

for data1, data2 in combinations:
    (x1, y1, z1), (vx1, vy1, vz1) = data1
    (x2, y2, z2), (vx2, vy2, vz2) = data2

    if vy2 * vx1 - vx2 * vy1 != 0:
        s = (y1 * vx1 + x2 * vy1 - x1 * vy1 - y2 * vx1) / (vy2 * vx1 - vx2 * vy1)
        t = (x2 - x1 + s * vx2) / vx1
        x = x2 + s * vx2
        y = y2 + s * vy2
        if s >= 0 and t >= 0 and test_area_min <= x <= test_area_max and test_area_min <= y <= test_area_max:
            intersections_in_test_area += 1
    else:
        s = None

print(intersections_in_test_area)
