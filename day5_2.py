f = open("inputs/day5.txt")
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
    for position, l in current_values:
        last_highest = position
        end_of_value = position + l
        remaining_length = l
        for entry in map_n:
            d_r, s_r, length = entry
            original_s_r = s_r
            if s_r < last_highest:
                length = max(length - (last_highest - s_r), 0)
                s_r = last_highest
            if last_highest < s_r and length > 0 and remaining_length > 0:
                value_length = min(s_r - last_highest, remaining_length)
                if value_length > 0:
                    next_values.append((last_highest, value_length))
                    last_highest = s_r
                    remaining_length -= value_length
            if last_highest <= s_r < end_of_value and length > 0 and remaining_length > 0:
                value_length = min(length, remaining_length)
                if value_length > 0:
                    next_values.append((last_highest + d_r - original_s_r, value_length))
                    last_highest = s_r + value_length
                    remaining_length -= value_length

        if remaining_length > 0:
            next_values.append((last_highest, remaining_length))
    current_values = next_values

print(sorted(current_values, key=lambda x: x[0])[0][0])
