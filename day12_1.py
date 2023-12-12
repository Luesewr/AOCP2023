import re

f = open("inputs/day12.txt")
lines = [line.split(" ") for line in f.read().split("\n")]
spring_strings, record_strings = list(zip(*lines))
springs = [re.sub(r'\.+', '.', spring) for spring in spring_strings]
records = [[int(i) for i in record.split(",")] for record in record_strings]
lines = zip(springs, records)


def bruteforce(spring, spring_index, record, record_index, known_spring_positions, lookup_table):
    if (spring_index, record_index) in lookup_table:
        return lookup_table[(spring_index, record_index)]
    record_length = record[record_index]
    next_spring = len(spring)
    if '#' in spring[spring_index:]:
        next_spring = spring.index('#', spring_index)
    t = 0
    for i in range(spring_index, next_spring + 1):
        ending_index = i + record_length - 1

        if ending_index >= len(spring):
            continue
        if '.' in spring[i:ending_index + 1]:
            continue
        if ending_index + 1 in known_spring_positions:
            continue

        if record_index == len(record) - 1 and ending_index < len(spring) and '#' not in spring[ending_index + 1:]:
            t += 1
        elif ending_index < len(spring) and record_index + 1 < len(record):
            result = bruteforce(spring, ending_index + 2, record, record_index + 1, known_spring_positions, lookup_table)
            t += result
            lookup_table[(ending_index + 2, record_index + 1)] = result

    return t


results = []

for spring, record in lines:
    spring_indices = {i for i in range(len(spring)) if spring[i] == '#'}
    results.append(bruteforce(spring, 0, record, 0, spring_indices, {}))

print(sum(results))
