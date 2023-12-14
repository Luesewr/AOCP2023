f = open("inputs/day14.txt")
rows = f.read().split("\n")
columns = [''.join(row) for row in list(zip(*rows))]

cycles_needed = 1000000000
skipped = False

known_states = {}
cycle = 0
while cycle < 4 * cycles_needed:
    if not skipped and cycle % 4 == 0:
        key = ''.join(rows)
        if key in known_states:
            cycle_size = cycle // 4 - known_states[key]
            skip_size = (cycles_needed - cycle // 4) // cycle_size
            cycle += skip_size * cycle_size * 4
            skipped = True
        else:
            known_states[key] = cycle // 4

    lines = columns if cycle % 2 == 0 else rows

    for index, line in enumerate(lines):
        if 1 < cycle % 4:
            line = line[::-1]
        new_line = ['.' for i in range(len(line))]
        last_anchor = 0
        length = 0
        for i, c in enumerate(line):
            if c == '#':
                new_line[i] = '#'
                for j in range(length):
                    new_line[last_anchor + j] = 'O'
                last_anchor = i + 1
                length = 0
            elif c == 'O':
                length += 1
        for j in range(length):
            new_line[last_anchor + j] = 'O'
        if 1 < cycle % 4:
            lines[index] = ''.join(new_line[::-1])
        else:
            lines[index] = ''.join(new_line)

    if cycle % 2 == 0:
        columns = lines
        rows = [''.join(row) for row in list(zip(*columns))]
    else:
        rows = lines
        columns = [''.join(column) for column in list(zip(*rows))]

    cycle += 1

score = 0

for column in columns:
    for i, c in enumerate(column):
        if c == 'O':
            score += len(column) - i

print(score)
