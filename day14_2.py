f = open("inputs/day14.txt")
rows = f.read().split("\n")
columns = [''.join(row) for row in list(zip(*rows))]

cycles_needed = 1000000000
skipped = False

known_states = {}
cycle = 0
while cycle < 2 * cycles_needed:
    key = ''.join(rows)
    if not skipped and cycle % 2 == 0 and key in known_states:
        cycle_size = cycle // 2 - known_states[key]
        skip_size = (cycles_needed - cycle // 2) // cycle_size
        cycle += skip_size * cycle_size * 2
        skipped = True
    elif cycle % 2 == 0:
        known_states[key] = cycle // 2

    for column_index, column in enumerate(columns):
        if cycle % 2 == 1:
            column = column[::-1]
        new_column = ['.' for i in range(len(column))]
        last_anchor = 0
        length = 0
        for i, c in enumerate(column):
            if c == '#':
                new_column[i] = '#'
                for j in range(length):
                    new_column[last_anchor + j] = 'O'
                last_anchor = i + 1
                length = 0
            elif c == 'O':
                length += 1
        for j in range(length):
            new_column[last_anchor + j] = 'O'
        if cycle % 2 == 0:
            columns[column_index] = ''.join(new_column)
        else:
            columns[column_index] = ''.join(new_column[::-1])
    rows = [''.join(row) for row in list(zip(*columns))]

    for row_index, row in enumerate(rows):
        if cycle % 2 == 1:
            row = row[::-1]
        new_row = ['.' for i in range(len(row))]
        last_anchor = 0
        length = 0
        for i, c in enumerate(row):
            if c == '#':
                new_row[i] = '#'
                for j in range(length):
                    new_row[last_anchor + j] = 'O'
                last_anchor = i + 1
                length = 0
            elif c == 'O':
                length += 1
        for j in range(length):
            new_row[last_anchor + j] = 'O'
        if cycle % 2 == 0:
            rows[row_index] = ''.join(new_row)
        else:
            rows[row_index] = ''.join(new_row[::-1])
    columns = [''.join(row) for row in list(zip(*rows))]
    cycle += 1


score = 0

for column in columns:
    for i, c in enumerate(column):
        if c == 'O':
            score += len(column) - i

print(score)
