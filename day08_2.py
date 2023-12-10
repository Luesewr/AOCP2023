from math import lcm

f = open("inputs/day8.txt")
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

    while current_node not in ending_nodes:
        current_instruction = instructions[current_instruction_index % len(instructions)]
        current_node = node_map[(current_node, current_instruction)]
        current_instruction_index += 1

        if current_node in ending_nodes:
            repeat_endings.append(current_instruction_index)

print(lcm(*repeat_endings))
