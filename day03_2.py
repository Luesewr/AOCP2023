f = open("inputs/day3.txt")
e = f.read().split("\n")
e_len = len(e)

t = 0

gears_map = {}

for i, s in enumerate(e):
    number = ""
    s_len = len(s)
    for j, c in enumerate(s):
        if c.isnumeric():
            number += c
            if j + 1 == s_len or not s[j + 1].isnumeric():
                n_len = len(number)
                start_x = max(0, j - n_len)
                start_y = max(0, i - 1)
                end_x = min(s_len - 1, j + 1)
                end_y = min(e_len - 1, i + 1)

                gears = []

                gear_adjacent = False

                for k in range(start_y, end_y + 1):
                    for l in range(start_x, end_x + 1):
                        if e[k][l] == '*':
                            gear_adjacent = True
                            gears.append((l, k))

                if gear_adjacent:
                    for gear in gears:
                        if gear in gears_map:
                            gears_map[gear].append(int(number))
                        else:
                            gears_map[gear] = [int(number)]
        else:
            number = ""
for v in gears_map.values():
    if len(v) == 2:
        t += v[0] * v[1]
print(t)
