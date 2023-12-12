import re

f = open("inputs/test_day12.txt")
lines = [line.split(" ") for line in f.read().split("\n")]
spring_strings, record_strings = list(zip(*lines))
springs = [re.sub(r'\.+', '.', spring) for spring in spring_strings]
records = [[int(i) for i in record.split(",")] for record in record_strings]
lines = zip(springs, records)


def try_options_from(springs_string, record, spring_index, record_index, spring_length, record_length):
    if record_length > spring_length:
        return 0
    t = 0
    while spring_index < len(spring_strings) and spring_strings[spring_index] == '.':
        spring_index += 1
    ending_index = spring_index + record[record_index]
    fits = springs_string[ending_index] != '#' if ending_index < len(record) else True
    if fits:
        for i in range(spring_index, ending_index):
            if springs_string[i] == '.':
                fits = False
                break
    if fits:
        print(spring_index, record_index)
        if record_index == len(record) - 1:
            print("returning 1")
            t = 1
        else:
            t += try_options_from(springs_string, record, spring_index + record[record_index] + 1, record_index + 1,
                                  spring_length - record[record_index] - 1, record_length - record[record_index])
    if springs_string[spring_index] != '#':
        t += try_options_from(springs_string, record, spring_index + 1, record_index, spring_length - 1, record_length)
    return t


for spring, record in lines:
    blocks = re.findall(r'(?:\?|#)+', spring)
    total_options_length = sum([len(match) for match in blocks])
    total_record_length = sum(record)
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
    print(try_options_from('.'.join(blocks), record, 0, 0, total_options_length, total_record_length))
