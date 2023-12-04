import re

f = open("inputs/day4.txt")
e = [re.sub('[ ]+', ' ', a).split(": ")[1] for a in f.read().split("\n")]
t = 0
for s in e:
    w, n = s.split(' | ')
    w = [int(i) for i in w.split(' ')]
    n = [int(i) for i in n.split(' ')]
    w.sort()
    n.sort()

    n_index = 0
    w_found = 0

    for w_n in w:
        while n_index < len(n) and n[n_index] < w_n:
            n_index += 1

        while n_index < len(n) and n[n_index] == w_n:
            w_found += 1
            n_index += 1
    if w_found > 0:
        t += 2**(w_found - 1)
print(t)
