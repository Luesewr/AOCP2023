import re

f = open("inputs/day19.txt")
workflows, parts = f.read().split('\n\n')
workflow_map = {}
t = 0
for workflow in workflows.split('\n'):
    name, conditions = workflow.split('{')
    condition_strings = conditions[:-1].split(',')
    workflow_logic = []
    for condition_string in condition_strings[:-1]:
        if_condition, result = condition_string.split(':')
        variable, value = re.split(r'[<>]', if_condition)
        operator = re.findall(r'[<>]', if_condition)[0]
        workflow_logic.append((variable, operator, int(value), result))
    workflow_map[name] = (workflow_logic, condition_strings[-1])

part_maps = []
for part in parts.split('\n'):
    part_map = {}
    variables = part[1:-1].split(',')
    for variable in variables:
        name, value = variable.split('=')
        part_map[name] = int(value)
    part_maps.append(part_map)

for part_map in part_maps:
    current_workflow = 'in'

    while current_workflow != 'A' and current_workflow != 'R':
        logic, else_value = workflow_map[current_workflow]
        found_match = False
        for condition in logic:
            variable, operator, value, result = condition
            if operator == '<':
                if part_map[variable] < value:
                    current_workflow = result
                    found_match = True
                    break
            if operator == '>':
                if part_map[variable] > value:
                    current_workflow = result
                    found_match = True
                    break
        if not found_match:
            current_workflow = else_value

    if current_workflow == 'A':
        t += sum(part_map.values())

print(t)
