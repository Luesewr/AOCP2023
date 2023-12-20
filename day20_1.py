from collections import deque

f = open("inputs/day20.txt")
lines = f.read().split('\n')
modules = {}
broadcaster = []

for line in lines:
    if line[0] == '%':
        name, connections_str = line[1:].split(' -> ')
        connections = connections_str.split(', ')
        modules[name] = ['%', False, connections]
    if line[0] == '&':
        name, connections_str = line[1:].split(' -> ')
        connections = connections_str.split(', ')
        modules[name] = ('&', {}, connections)
    if line[0:11] == 'broadcaster':
        broadcaster = line[1:].split(' -> ')[1].split(', ')

for name, module in modules.items():
    for connection in module[2]:
        if connection in modules and modules[connection][0] == '&':
            modules[connection][1][name] = False

pulse_queue = deque()
low_pulses = 0
high_pulses = 0

for _ in range(1000):
    for connection in broadcaster:
        pulse_queue.append((connection, False, 'broadcaster'))

    low_pulses += 1

    while len(pulse_queue) > 0:
        current_name, pulse_type, origin = pulse_queue.popleft()

        if pulse_type:
            high_pulses += 1
        else:
            low_pulses += 1

        if current_name in modules:
            current_module = modules[current_name]
        else:
            continue

        if current_module[0] == '%':
            if not pulse_type:
                current_module[1] = not current_module[1]
                for connection in current_module[2]:
                    pulse_queue.append((connection, current_module[1], current_name))

        if current_module[0] == '&':
            if origin in current_module[1]:
                current_module[1][origin] = pulse_type
            all_high = all(last_pulse is True for last_pulse in current_module[1].values())

            for connection in current_module[2]:
                pulse_queue.append((connection, not all_high, current_name))

print(low_pulses * high_pulses)
