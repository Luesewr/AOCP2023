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
    counts_amount = [[] for _ in range(5)]
    joker_count = 0
    for val, count in counts:
        if val == 'J':
            joker_count += count
        counts_amount[5 - count].append(val)
    if 0 < joker_count < 5:
        a = list(map(lambda x: len(list(filter(lambda y: y != 'J', x))) > 0, counts_amount)).index(True)
        amounts = counts_amount[a]
        non_joker_counts = filter(lambda x: x != 'J', amounts)
        replacement_value = max(non_joker_counts, key=lambda x: value_lookup[x])
        amounts.remove(replacement_value)
        counts_amount[a - joker_count].append(replacement_value)
        counts_amount[5 - joker_count].remove('J')
    count_amounts = [len(_) for _ in counts_amount]

    header = '0x{}{}{}{}{}'.format(*count_amounts)
    number = '{}{}'.format(header, ''.join([value_lookup[_] for _ in hand[0]]))
    return int(number, 16)


e.sort(key=hand_to_value)
t = sum(map(lambda x: (x + 1) * e[x][1], range(len(e))))
print(t)
