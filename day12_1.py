import re

# 6009 too low

f = open("inputs/test_day12.txt")
lines = [line.split(" ") for line in f.read().split("\n")]
spring_strings, record_strings = list(zip(*lines))
springs = [re.sub(r'\.+', '.', spring) for spring in spring_strings]
records = [[int(i) for i in record.split(",")] for record in record_strings]
lines = zip(springs, records)


def try_options_from(spring_blocks, record, spring_index, inner_spring_index, record_index, inner_record_index):
    print(spring_index, inner_spring_index, record_index)
    if inner_record_index > 0:
        print("inner record index:", inner_record_index)
    if record_index >= len(record):
        print("got to the end of the records")
        return 1
    t = 0
    updated = True
    skipped_over_spring = False
    while updated:
        updated = False
        if spring_index < len(spring_blocks) and spring_blocks[spring_index][0] == '.':
            spring_index += 1
            updated = True
            if inner_record_index > 0:
                print("found a dot when progressing during search")
                return 0

        while spring_index < len(spring_blocks) and inner_spring_index >= len(spring_blocks[spring_index]):
            if skipped_over_spring:
                print("skipped over spring")
                return 0
            inner_spring_index -= len(spring_blocks[spring_index])
            spring_index += 1
            if not skipped_over_spring and spring_index < len(spring_blocks) and spring_blocks[spring_index][0] == '#':
                skipped_over_spring = True
                print("marked as spring skipper")
            updated = True

    if spring_index >= len(spring_blocks):
        print("ran out of spring, could not find all records")
        return 0

    print(spring_index, inner_spring_index, record_index)

    record_length_remaining = record[record_index] - inner_record_index - 1 if inner_record_index > 0 else record[record_index] - 1

    ending_index = min(inner_spring_index + record_length_remaining, len(spring_blocks[spring_index]) - 1)
    print("ending index: ", ending_index)
    remaining_search_length = inner_spring_index + record_length_remaining - ending_index
    print("remaining search: ", remaining_search_length)
    if remaining_search_length > 0:
        print("spring too short, looking at next spring")
        t += try_options_from(spring_blocks, record, spring_index + 1, 0, record_index, record[record_index] - record_length_remaining)
    elif remaining_search_length == 0 and record_index + 1 < len(record) and (spring_blocks[spring_index][0] == '?' or (spring_blocks[spring_index][0] == '#' and ending_index == len(spring_blocks[spring_index]) - 1)):
        print("found match, looking for next record")
        t += try_options_from(spring_blocks, record, spring_index, ending_index + 2, record_index + 1, 0)
    elif remaining_search_length == 0 and record_index + 1 == len(record) and spring_blocks[spring_index][0] != '.':
        print("search done, adding one")
        t += 1
    if spring_blocks[spring_index][0] != '#' or (spring_blocks[spring_index][0] != '#' and inner_spring_index == len(spring_blocks[spring_index]) - 1):
        print("going one further, just to check")
        t += try_options_from(spring_blocks, record, spring_index, inner_spring_index + 1, record_index, 0)
    return t

results = []

for spring, record in lines:
    # print(spring)
    blocks = re.findall(r'\.+|#+|\?+', spring)
    # print(blocks)
    total_options_length = sum([len(match) for match in blocks])
    total_record_length = len(spring)
    while '#' in blocks[-1] and len(blocks[-1]) == record[-1]:
        blocks.pop()
        length = record.pop()
        total_options_length -= length
        total_record_length -= length
    while '#' in blocks[0] and len(blocks[0]) == record[0]:
        blocks.pop(0)
        length = record.pop(0)
        total_options_length -= length
        total_record_length -= length

    print(blocks)
    results.append(try_options_from(blocks, record, 0, 0, 0, 0))

print(results)
print(sum(results))