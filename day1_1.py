f = open("inputs/day1.txt")
e = f.read().split("\n")
n = [list(filter(lambda x: x.isnumeric(), [*a])) for a in e]
t = 0
for a in n:
    t += int(a[0] + a[-1])
print(t)
