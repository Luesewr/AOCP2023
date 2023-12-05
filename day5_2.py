f = open("inputs/test_day5.txt")
e = f.read().split("\n\n")
seed_pairs = [int(i) for i in e[0].split(": ")[1].split(" ")]
it = iter(seed_pairs)
seeds = sorted(list(zip(it, it)), key=lambda x: x[0])
maps = e[1:]
maps = [sorted([[int(k) for k in j.split(" ")] for j in i.split("\n")[1:]], key=lambda x: x[1]) for i in maps]
locations = []

current_values = seeds
for map_n in maps:
    next_values = []
    for current_value in current_values:
        last_highest = current_value[0]
        end_of_value = current_value[0] + current_value[1]
        remaining_length = current_value[1]
        for entry in map_n:
            d_r, s_r, length = entry
            if s_r < last_highest:
                length -= last_highest - s_r
                s_r = last_highest
            if last_highest < s_r:
                value_length = min(s_r - last_highest, remaining_length)
                if value_length > 0:
                    next_values.append((last_highest, value_length))
                    last_highest = s_r
                    remaining_length -= value_length
            if last_highest <= s_r < end_of_value:
                value_length = min(length, remaining_length)
                if value_length > 0:
                    next_values.append((last_highest + d_r - s_r, value_length))
                    last_highest = s_r + value_length
                    remaining_length -= value_length
            print(last_highest, remaining_length)
            print("values: ", next_values)

        if remaining_length > 0:
            next_values.append((last_highest, remaining_length))
    current_values = next_values
    break



print(current_values)
