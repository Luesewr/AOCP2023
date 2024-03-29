import random
from collections import Counter
from functools import reduce
from operator import mul

f = open("inputs/day25.txt")
lines = [line.split(': ') for line in f.read().split('\n')]
components = [(name, connections.split(' ')) for name, connections in lines]
index = 0
component_indices = {}
component_names = []
edges = []

for name, connections in components:
    if name not in component_indices:
        component_indices[name] = index
        component_names.append(name)
        index += 1

    component_index = component_indices[name]
    for connection in connections:
        if connection not in component_indices:
            component_indices[connection] = index
            component_names.append(connection)
            index += 1

        connection_index = component_indices[connection]
        edges.append((component_index, connection_index))


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            return True
        return False

    def find_all(self):
        for i in range(len(self.parent)):
            self.find(i)

    def reset(self):
        size = len(self.parent)
        self.parent = [i for i in range(size)]
        self.rank = [0] * size


edge_counts = {edge: 0 for edge in edges}
checked_counts = set()
union_find = UnionFind(index)

while True:
    random.shuffle(edges)

    for u, v in edges:
        if union_find.union(u, v):
            edge_counts[(u, v)] += 1

    union_find.reset()

    for u, v in edges[::-1]:
        if union_find.union(u, v):
            edge_counts[(u, v)] += 1

    union_find.reset()

    counts = sorted(edge_counts.items(), key=lambda edge_count_item: edge_count_item[1], reverse=True)[:3]

    counts.sort()

    counts_tuple = tuple([edge for edge, count in counts])

    if counts_tuple not in checked_counts:
        checked_counts.add(counts_tuple)

        for u, v in edges:
            if (u, v) in counts_tuple:
                continue

            union_find.union(u, v)

        union_find.find_all()
        if len(set(union_find.parent)) == 2:
            parent_counts = Counter(union_find.parent)
            print(reduce(mul, parent_counts.values()))
            break

        union_find.reset()
