f = open("inputs/day7.txt")
e = [(a.split(" ")[0], int(a.split(" ")[1])) for a in f.read().split("\n")]
value_lookup = {'T': 'A', 'J': '1', 'Q': 'C', 'K': 'D', 'A': 'E'}
for i in range(2, 10):
    value_lookup[str(i)] = str(i)


def hand_to_value(hand):
    counts = {}
    for c in hand[0]:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    counts_amount = {a + 1: [] for a in range(5)}
    joker_count = 0
    for val, count in counts:
        if val == 'J':
            joker_count += count
        counts_amount[count].append(val)
    if joker_count > 0:
        for a in range(5, 0, -1):
            non_joker_counts = list(filter(lambda x: x != 'J', counts_amount[a]))
            if len(non_joker_counts) > 0:
                replacement_value = sorted(non_joker_counts, key=lambda x: value_lookup[x])[-1]
                counts_amount[a].remove(replacement_value)
                counts_amount[a + joker_count].append(replacement_value)
                counts_amount[joker_count].remove('J')
                break
    count_amounts = [len(counts_amount[a]) for a in range(5, 0, -1)]

    header = '0x{}{}{}{}{}'.format(*count_amounts)
    number = '{}{}'.format(header, ''.join([value_lookup[a] for a in hand[0]]))
    return int(number, 16)


e.sort(key=hand_to_value)
t = 0
for index, value in enumerate(e):
    t += value[1] * (index + 1)
print(t)
