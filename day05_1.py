f = open("inputs/day5.txt")
e = f.read().split("\n\n")
seeds = [int(i) for i in e[0].split(": ")[1].split(" ")]
maps = e[1:]
maps = [[[int(k) for k in j.split(" ")] for j in i.split("\n")[1:]] for i in maps]
locations = []

for seed in seeds:
    current_value = seed
    for map_n in maps:
        next_value = current_value
        for entry in map_n:
            d_r, s_r, length = entry
            if s_r <= current_value < s_r + length:
                next_value += d_r - s_r
                break
        current_value = next_value

    locations.append(current_value)
print(min(locations))
