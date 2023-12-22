f = open("inputs/day22.txt")
lines = f.read().split('\n')


class Block:
    def __init__(self, starting, ending):
        self.start_pos = [int(i) for i in starting.split(',')]
        self.ending_pos = [int(i) for i in ending.split(',')]
        self.supporting = set()
        self.supported = set()

    def __repr__(self):
        return f'Block({self.start_pos}, {self.ending_pos})'


def simulate_fall(block, falling):
    if block in falling:
        return
    if block.supported.intersection(falling) == block.supported:
        falling.add(block)
        [simulate_fall(supporting_block, falling) for supporting_block in block.supporting]

blocks = [Block(*line.split('~')) for line in lines]

max_x_block = max(blocks, key=lambda block: max(block.start_pos[0], block.ending_pos[0]))
max_x = max(max_x_block.start_pos[0], max_x_block.ending_pos[0])
max_y_block = max(blocks, key=lambda block: max(block.start_pos[1], block.ending_pos[1]))
max_y = max(max_y_block.start_pos[1], max_y_block.ending_pos[1])
max_z_block = max(blocks, key=lambda block: max(block.start_pos[2], block.ending_pos[2]))
max_z = max(max_z_block.start_pos[2], max_z_block.ending_pos[2])

highest_points = [[(0, None) for j in range(max_y + 1)] for i in range(max_x + 1)]

blocks.sort(key=lambda block: block.start_pos[2])

for block in blocks:
    d_z = block.ending_pos[2] - block.start_pos[2] + 1

    highest_z = 0

    supported = set()

    for y in range(block.start_pos[1], block.ending_pos[1] + 1):
        for x in range(block.start_pos[0], block.ending_pos[0] + 1):
            if highest_points[x][y][0] > highest_z:
                highest_z = highest_points[x][y][0]
                supported = set()
            if highest_points[x][y][0] == highest_z and highest_points[x][y][1] is not None:
                supported.add(highest_points[x][y][1])

    block.supported = supported
    for supported_block in supported:
        supported_block.supporting.add(block)

    for y in range(block.start_pos[1], block.ending_pos[1] + 1):
        for x in range(block.start_pos[0], block.ending_pos[0] + 1):
            highest_points[x][y] = (highest_z + d_z, block)

t = 0
for block in blocks:
    would_fall = 0
    falling_set = {block}
    for supporting_block in block.supporting:
        simulate_fall(supporting_block, falling_set)
    t += len(falling_set) - 1
print(t)
