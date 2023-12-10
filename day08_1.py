f = open("inputs/day8.txt")
instructions, e = f.read().split("\n\n")
start = "AAA"
end = "ZZZ"
node_map = {}

for line in e.split("\n"):
    node_name, connections = line.split(" = ")
    left_name, right_name = connections[1:-1].split(", ")
    node_map[(node_name, "L")] = left_name
    node_map[(node_name, "R")] = right_name

current_node = start
current_instruction_index = 0

while current_node != end:
    current_instruction = instructions[current_instruction_index % len(instructions)]
    current_node = node_map[(current_node, current_instruction)]
    current_instruction_index += 1

print(current_instruction_index)
