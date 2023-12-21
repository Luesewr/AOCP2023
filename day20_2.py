from math import lcm
from collections import deque

class PulseModule:
    def __init__(self, module_name, module_type, connections):
        self.module_name = module_name
        self.module_type = module_type
        self.connections = connections
        self.state = False
        self.low_count = 0
        self.incoming_modules = []
        self.cycle = None

    def __repr__(self):
        return str(self.module_name)


f = open("inputs/day20.txt")
lines = f.read().split('\n')
modules = {}

for line in lines:
    if line[0] == '%':
        name, connections_str = line[1:].split(' -> ')
        connections = connections_str.split(', ')
        modules[name] = PulseModule(name, '%', connections)
    elif line[0] == '&':
        name, connections_str = line[1:].split(' -> ')
        connections = connections_str.split(', ')
        modules[name] = PulseModule(name, '&', connections)
    else:
        name, connections_str = line.split(' -> ')
        connections = connections_str.split(', ')
        modules['broadcaster'] = PulseModule('broadcaster', 'broadcaster', line.split(' -> ')[1].split(', '))

modules['rx'] = PulseModule('rx', '%', [])

for module in modules.values():
    for connection in module.connections:
        if connection in modules:
            modules[connection].incoming_modules.append(module.module_name)


def create_local_tree(current_module, visited):
    # print(current_module.incoming_modules)
    if current_module in visited:
        return set()

    visited.add(current_module)

    tree = set()
    tree.add(current_module)

    for module in current_module.incoming_modules:
        tree = tree.union(create_local_tree(modules[module], visited))

    return tree


def calculate_cycle(current_module):
    if current_module.module_name == 'rx':
        return calculate_cycle(modules[current_module.incoming_modules[0]])
    elif current_module.module_type == '&' and all(modules[m].module_type == '&' for m in current_module.incoming_modules):
        return lcm(*[calculate_cycle(modules[modules[m].incoming_modules[0]]) for m in current_module.incoming_modules])
    elif current_module.module_type == '&':
        tree_set = create_local_tree(current_module, set())
        button_presses = 0
        state_changed = False
        module_queue = deque()
        while not (not current_module.state and state_changed):
            button_presses += 1
            for connection in modules['broadcaster'].connections:
                module_queue.append((modules[connection], 'broadcaster'))
            while len(module_queue) > 0 and not (not current_module.state and state_changed):
                m, origin = module_queue.popleft()
                if m not in tree_set:
                    continue

                can_send = True

                if m.module_type == '%':
                    if not modules[origin].state:
                        m.state = not m.state
                    else:
                        can_send = False
                elif m.module_type == '&':
                    m.state = not all(modules[incoming].state for incoming in m.incoming_modules)
                    if m.state and m == current_module:
                        state_changed = True
                if can_send:
                    for connection in m.connections:
                        module_queue.append((modules[connection], m.module_name))
        return button_presses
    print(current_module)


print(calculate_cycle(modules['rx']))
