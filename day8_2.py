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

        if current_node[-1] == 'Z':
            ending_indices.append(current_instruction_index)

        current_instruction_index += 1

    loop_index = visited_nodes.index(current_node)
    repeat_endings.append(((loop_index, current_instruction_index - loop_index), list(map(lambda _: _ - loop_index + 1, ending_indices))))

print(lcm(*list(map(lambda _: _[1][0] + _[0][0], repeat_endings))))