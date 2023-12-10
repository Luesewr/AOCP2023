from itertools import product
from math import gcd, ceil, sqrt
from functools import reduce


def chinese_remainder(m, a):
    sum = 0
    prod = reduce(lambda acc, b: acc * b, m)
    for n_i, a_i in zip(m, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def divisors(n):
    lis = []
    s = ceil(sqrt(n))
    for g in range(s, 0, -1):
        if n % g == 0:
            lis.append(g)
            lis.append(int(n / g))
    return set(lis)


f = open("inputs/test_day8.txt")
instructions, e = f.read().split("\n\n")
node_map = {}

for line in e.split("\n"):
    node_name, connections = line.split(" = ")
    left_name, right_name = connections[1:-1].split(", ")
    node_map[(node_name, "L")] = left_name
    node_map[(node_name, "R")] = right_name

unique_nodes = {key[0] for key in node_map.keys()}

starting_nodes = list(filter(lambda _: _[-1] == 'A', unique_nodes))
ending_nodes = set(filter(lambda _: _[-1] == 'Z', unique_nodes))

repeat_endings = []

for node in starting_nodes:

    current_instruction_index = 0
    current_node = node
    visited_nodes = []
    endings = []

    while current_node not in visited_nodes[(current_instruction_index % len(instructions))::len(instructions)]:

        visited_nodes.append(current_node)
        current_instruction = instructions[current_instruction_index % len(instructions)]
        current_node = node_map[(current_node, current_instruction)]
        current_instruction_index += 1

        if current_node[-1] == 'Z':
            endings.append(current_instruction_index)

    offset = visited_nodes.index(current_node)
    loop_length = len(visited_nodes) - offset
    repeat_endings.append((loop_length, list(map(lambda _: _, endings))))

loop_lengths = [loop_length for loop_length, data in repeat_endings]

print(repeat_endings)

original_loop_lengths = loop_lengths

is_coprime = gcd(*loop_lengths) == 0

while not is_coprime:
    is_coprime = True
    denominator_count = {}
    denominators = []

    for index, loop_length in enumerate(loop_lengths):
        loop_divisors = list(divisors(loop_length))
        denominators.append(loop_divisors)

        for x in loop_divisors:
            if x in denominator_count:
                denominator_count[x] += 1
            else:
                denominator_count[x] = 1

    common_factors = list(filter(lambda item: item[1] > 1 and item[0] != 1, denominator_count.items()))
    if len(common_factors) > 0:
        is_coprime = False

        biggest_common_factor = common_factors[-1][0]

        lengths_and_denominators = list(zip(zip(range(len(loop_lengths)), loop_lengths), denominators))
        # print(lengths_and_denominators)
        least_denoms_with_factor = min(filter(lambda l_d: biggest_common_factor in l_d[1], lengths_and_denominators), key=lambda l_d: len(l_d[1]))
        # print(least_denoms_with_factor)
        (index, loop_length), denoms = least_denoms_with_factor
        loop_lengths[index] //= biggest_common_factor

print(loop_lengths)

endings = [endings for loop_length, endings in repeat_endings]
combinations = list(product(*endings))
original_loop_product = reduce(lambda acc, b: acc * b, original_loop_lengths)
min_intersection = 100000000000000
#
for combination in combinations:
    offset_combination = combination
    combination_offset = 0
    while (intersection := chinese_remainder(loop_lengths, offset_combination)) == 0:
        offset_combination = [i + 1 for i in offset_combination]
        combination_offset -= 1
    loop_product = reduce(lambda acc, b: acc * b, loop_lengths)
    all_match = False
    while not all_match and intersection <= original_loop_product:
        all_match = True
        for loop_length, offset in zip(loop_lengths, list(offset_combination)):
            if (intersection - offset) % loop_length != 0:
                all_match = False
                intersection += loop_product
                break
    #
    if all_match:
        print(intersection)
        min_intersection = min(min_intersection, intersection + combination_offset)
#
print(min_intersection)
