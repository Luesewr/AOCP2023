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
ending_nodes = list(filter(lambda _: _[-1] == 'Z', unique_nodes))

repeat_endings = []

for node in starting_nodes:

    current_instruction_index = 0
    current_node = node
    visited_nodes = []
    ending_indices = []

    while current_node not in visited_nodes[(current_instruction_index % len(instructions))::(len(instructions))]:
        visited_nodes.append(current_node)
        current_instruction = instructions[current_instruction_index % len(instructions)]
        current_node = node_map[(current_node, current_instruction)]

        if current_node in ending_nodes:
            ending_indices.append(current_instruction_index)

        current_instruction_index += 1

    repeat_endings.append(ending_indices[0] + 1)

print(lcm(*repeat_endings))
