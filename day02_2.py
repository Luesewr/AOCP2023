f = open("inputs/day2.txt")
e = [a.split(": ")[1].split("; ") for a in f.read().split("\n")]
total = 0
for game in e:
    minimums = {"red": 0, "green": 0, "blue": 0}
    valid = True
    for collection in game:
        amounts = collection.split(", ")
        for amount in amounts:
            n, c = amount.split(" ")
            minimums[c] = max(minimums[c], int(n))
    power = 1
    for value in minimums.values():
        power *= value
    total += power
print(total)
