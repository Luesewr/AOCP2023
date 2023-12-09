from itertools import product
from math import lcm, gcd

def mod_inverse(a, m):
    x = gcd(a, m)
    return (x % m + m) % m

def chinese_remainder_theorem(n, a):
    # n = list of moduli
    # a = list of remainders

    # Calculate N
    N = 1
    for i in n:
        N *= i

    result = 0
    for i in range(len(n)):
        Ni = N // n[i]
        inv = mod_inverse(Ni, n[i])
        result += a[i] * Ni * inv

    return ((result - 1) % lcm(*n)) + 1


f = open("inputs/modified_day8.txt")
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

endings = [endings for loop_length, endings in repeat_endings]
combinations = list(product(*endings))

min_intersection = 0

for combination in combinations:
    loop_lengths = [loop_length for loop_length, data in repeat_endings]
    intersection = chinese_remainder_theorem(loop_lengths, list(combination))
    min_intersection = max(min_intersection, intersection)

print(min_intersection)
