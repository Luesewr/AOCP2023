f = open("inputs/day2.txt")
e = [a.split(": ")[1].split("; ") for a in f.read().split("\n")]
allowed = {"red": 12, "green": 13, "blue": 14}
total = 0
for index, game in enumerate(e):
    valid = True
    for collection in game:
        amounts = collection.split(", ")
        for amount in amounts:
            n, c = amount.split(" ")
            if int(n) > allowed[c]:
                valid = False
    if valid:
        total += index + 1
print(total)
