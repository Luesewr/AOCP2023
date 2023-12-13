f = open("inputs/day13.txt")
mirrors = f.read().split("\n\n")
mirror_rows = [mirror.split("\n") for mirror in mirrors]
mirror_columns = [[''.join(column) for column in list(zip(*rows))] for rows in mirror_rows]

scores = [0 for i in range(len(mirrors))]

for index in range(len(mirrors)):
    row = mirror_rows[index]
    for i in range(1, len(row)):
        min_distance = min(i, len(row) - i)
        tolerance = 1
        for j in range(min_distance):
            tolerance -= sum([0 if c1 == c2 else 1 for c1, c2 in zip(row[i - 1 - j], row[i + j])])
        if tolerance == 0:
            scores[index] = i * 100

    column = mirror_columns[index]
    for i in range(1, len(column)):
        min_distance = min(i, len(column) - i)
        tolerance = 1
        for j in range(min_distance):
            tolerance -= sum([0 if c1 == c2 else 1 for c1, c2 in zip(column[i - 1 - j], column[i + j])])
        if tolerance == 0:
            scores[index] = i

print(sum(scores))
