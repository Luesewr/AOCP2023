f = open("inputs/day14.txt")
rows = f.read().split("\n")
columns = [''.join(row) for row in list(zip(*rows))]

cycles_needed = 1000000000
skipped = False

known_states = {}
cycle = 0
while cycle < cycles_needed:
    if not skipped:
        key = ''.join(rows)
        if key in known_states:
            cycle_size = cycle - known_states[key]
            skip_size = (cycles_needed - cycle) // cycle_size
            cycle += skip_size * cycle_size
            skipped = True
        else:
            known_states[key] = cycle

    for inner_cycle in range(4):
        lines = columns if inner_cycle % 2 == 0 else rows

        for index, line in enumerate(lines):
            if 1 < inner_cycle % 4:
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
            if 1 < inner_cycle % 4:
                lines[index] = ''.join(new_line[::-1])
            else:
                lines[index] = ''.join(new_line)

        if inner_cycle % 2 == 0:
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
