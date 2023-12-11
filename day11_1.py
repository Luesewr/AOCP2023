from itertools import combinations

f = open("inputs/day11.txt")
lines = f.read().split("\n")
empty_rows = [i for i in range(len(lines)) if '#' not in lines[i]]
columns = list(zip(*lines))
empty_columns = [i for i in range(len(columns)) if '#' not in columns[i]]
galaxies = []
current_y = 0
for y in range(len(lines)):
    if y in empty_rows:
        current_y += 2
        continue

    current_x = 0
    for x in range(len(columns)):
        if x in empty_columns:
            current_x += 2
            continue
        if columns[x][y] == '#':
            galaxies.append((current_x, current_y))
        current_x += 1
    current_y += 1

combinations = list(combinations(galaxies, 2))
t = sum([abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1]) for galaxy1, galaxy2 in combinations])
print(t)
