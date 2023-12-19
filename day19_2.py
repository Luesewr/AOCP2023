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

part_maps = [('in', 0, {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)})]

while len(part_maps) > 0:
    current_workflow, condition_index, current_part_map = part_maps.pop()

    if current_workflow == 'R':
        continue

    if current_workflow == 'A':
        min_x, max_x = current_part_map['x']
        min_m, max_m = current_part_map['m']
        min_a, max_a = current_part_map['a']
        min_s, max_s = current_part_map['s']
        t += (max_x - min_x + 1) * (max_m - min_m + 1) * (max_a - min_a + 1) * (max_s - min_s + 1)
        continue

    logic, else_value = workflow_map[current_workflow]
    found_match = False

    variable, operator, value, result = logic[condition_index]
    part_value_min, part_value_max = current_part_map[variable]
    if operator == '<':
        if part_value_min < value <= part_value_max:
            new_part_map_lt = current_part_map.copy()
            new_part_map_lt[variable] = (part_value_min, value - 1)
            part_maps.append((result, 0, new_part_map_lt))
            current_part_map[variable] = (value, part_value_max)
            if condition_index + 1 < len(logic):
                part_maps.append((current_workflow, condition_index + 1, current_part_map))
            else:
                part_maps.append((else_value, 0, current_part_map))
        elif part_value_min < value and part_value_max < value:
            new_part_map_lt = current_part_map.copy()
            new_part_map_lt[variable] = (part_value_min, part_value_max)
            part_maps.append((result, 0, new_part_map_lt))
        elif value <= part_value_min and value <= part_value_max:
            if condition_index + 1 < len(logic):
                part_maps.append((current_workflow, condition_index + 1, current_part_map))
            else:
                part_maps.append((else_value, 0, current_part_map))

    if operator == '>':
        if part_value_min <= value < part_value_max:
            new_part_map_gt = current_part_map.copy()
            new_part_map_gt[variable] = (value + 1, part_value_max)
            part_maps.append((result, 0, new_part_map_gt))
            current_part_map[variable] = (part_value_min, value)
            if condition_index + 1 < len(logic):
                part_maps.append((current_workflow, condition_index + 1, current_part_map))
            else:
                part_maps.append((else_value, 0, current_part_map))
        elif part_value_min <= value and part_value_max <= value:
            if condition_index + 1 < len(logic):
                part_maps.append((current_workflow, condition_index + 1, current_part_map))
            else:
                part_maps.append((else_value, 0, current_part_map))

        elif value < part_value_min and value < part_value_max:
            new_part_map_lt = current_part_map.copy()
            new_part_map_lt[variable] = (part_value_min, part_value_max)
            part_maps.append((result, 0, new_part_map_lt))

print(t)
