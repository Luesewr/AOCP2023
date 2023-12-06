import re
import math

f = open("inputs/day6.txt")
e = re.sub(" +", " ", f.read()).split("\n")
times = [int(i) for i in e[0].split("Time: ")[1].split(" ")]
distances = [int(i) for i in e[1].split("Distance: ")[1].split(" ")]

t = 1

for time, dist in zip(times, distances):
    d = time**2 - 4 * (dist + 1)
    low = math.ceil(time / 2 - math.sqrt(d) / 2)
    high = math.floor(time / 2 + math.sqrt(d) / 2)
    t *= high - low + 1

print(t)