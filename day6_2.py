import re
import math

f = open("inputs/day6.txt")
e = re.sub(" +", "", f.read()).split("\n")
time = int(e[0].split("Time:")[1])
distance = int(e[1].split("Distance:")[1])

print(math.floor(math.sqrt(time**2 - 4 * (distance + 1))))