f = open("inputs/day9.txt")
sequences = [[int(i) for i in s.split(" ")] for s in f.read().split("\n")]
t = 0

for sequence in sequences:
    current_sequence = sequence
    index = 0

    while len(list(filter(lambda x: x == 0, current_sequence))) != len(current_sequence):
        t += current_sequence[0] * (1 if index % 2 == 0 else -1)
        new_sequence = []
        for i in range(len(current_sequence) - 1):
            new_sequence.append(current_sequence[i + 1] - current_sequence[i])
        current_sequence = new_sequence
        index += 1

print(t)
