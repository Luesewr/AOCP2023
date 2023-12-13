f = open("inputs/day13.txt")
mirrors = f.read().split("\n\n")
mirror_rows = [mirror.split("\n") for mirror in mirrors]
mirror_columns = [[''.join(column) for column in list(zip(*rows))] for rows in mirror_rows]

scores = [0 for i in range(len(mirrors))]

for index in range(len(mirrors)):
    rows = mirror_rows[index]
    for i in range(1, len(rows)):
        min_distance = min(i, len(rows) - i)
        if rows[i - min_distance:i] == rows[i:i + min_distance][::-1]:
            scores[index] = i * 100
            break
    column = mirror_columns[index]
    for i in range(1, len(column)):
        min_distance = min(i, len(column) - i)
        if column[i - min_distance:i] == column[i:i + min_distance][::-1]:
            scores[index] = i
            break

print(sum(scores))
