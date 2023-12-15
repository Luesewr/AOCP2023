f = open("inputs/day15.txt")
strings = f.read().split(",")

hash_sum = 0

for s in strings:
    value = 0
    for c in s:
        value += ord(c)
        value *= 17
        value %= 256
    hash_sum += value

print(hash_sum)
