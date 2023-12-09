f = open("inputs/day9.txt")
sequences = [[int(i) for i in s.split(" ")] for s in f.read().split("\n")]
t = 0

for sequence in sequences:
    current_sequences = [sequence]
    current_sequence = sequence

    while len(list(filter(lambda x: x == 0, current_sequence))) != len(current_sequence):
        new_sequence = []
        for i in range(len(current_sequence) - 1):
            new_sequence.append(current_sequence[i + 1] - current_sequence[i])
        current_sequence = new_sequence
        current_sequences.append(new_sequence)

    extrapolate = 0

    for seq in current_sequences[::-1][1::]:
        extrapolate += seq[-1]
    t += extrapolate

print(t)
