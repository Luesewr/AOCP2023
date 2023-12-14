f = open("inputs/day14.txt")
lines = f.read().split("\n")
columns = [''.join(row) for row in list(zip(*lines))]

score = 0

for column in columns:
    last_anchor = 0
    length = 0
    for i, c in enumerate(column):
        if c == '#':
            last_anchor = i + 1
            length = 0
        elif c == 'O':
            score += len(column) - (last_anchor + length)
            length += 1

print(score)
