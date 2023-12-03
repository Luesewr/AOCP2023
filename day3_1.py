f = open("inputs/day3.txt")
e = f.read().split("\n")
e_len = len(e)

t = 0

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

                adjacent = False

                for k in range(start_y, end_y + 1):
                    for l in range(start_x, end_x + 1):
                        if not e[k][l].isnumeric() and e[k][l] != '.':
                            adjacent = True
                            break
                    if adjacent:
                        break

                if adjacent:
                    t += int(number)
        else:
            number = ""
print(t)
