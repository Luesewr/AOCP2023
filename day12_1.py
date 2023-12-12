import re

f = open("inputs/test_day12.txt")
lines = [line.split(" ") for line in f.read().split("\n")]
spring_strings, record_strings = list(zip(*lines))
springs = [re.sub(r'\.+', '.', spring) for spring in spring_strings]
records = [[int(i) for i in record.split(",")] for record in record_strings]
lines = zip(springs, records)


def try_options_from(spring_blocks, record, spring_index, inner_spring_index, record_index, search_length):

    t = 0
    while spring_index < len(spring_strings) and spring_blocks[spring_index][0] == '.':
        spring_index += 1
        if search_length > 0:
            return 0
    if spring_index >= len(spring_blocks):
        return 0

    ending_index = min(inner_spring_index + record[record_index], len(spring_blocks[spring_index]) - 1)
    remaining_search_length = inner_spring_index + record[record_index] - ending_index
    fits = True
    if fits:
        if remaining_search_length == 0 and spring_blocks[spring_index][0] == '#' and ending_index != len(spring_blocks[spring_index]) - 1:
            fits = False
    if fits:
        print(spring_index, record_index)
        if record_index == len(record) - 1:
            print("returning 1")
            t = 1
        elif remaining_search_length > 0:
            t + try_options_from(spring_blocks, record, spring_index + 1, 0, record_index, remaining_search_length)
        elif remaining_search_length == 0:
            t += try_options_from(spring_blocks, record, spring_index, ending_index + 1,
                                  record_index + 1, 0)
    if spring_blocks[spring_index] != '#':
        t += try_options_from(spring_blocks, record, spring_index, inner_spring_index + 1, record_index, 0)
    return t


for spring, record in lines:
    # print(spring)
    blocks = re.findall(r'\.+|#+|\?+', spring)
    print(blocks)
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
    print(try_options_from(blocks, record, 0, 0, 0, 0))
