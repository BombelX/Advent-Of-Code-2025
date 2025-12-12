from collections import defaultdict


def build_graph(lines):
    graph = defaultdict(list)
    for raw in lines:
        if not raw.strip():
            continue
        left, right = raw.split(':', 1)
        node = left.strip()
        targets = right.strip()
        if targets:
            graph[node].extend(targets.split())
    return graph


def count_paths(graph, start, target):
    def dfs(node, visited):
        if node == target:
            return 1
        total = 0
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                total += dfs(neighbor, visited)
                visited.remove(neighbor)
        return total

    return dfs(start, {start})


with open('day11/part1/data.txt', 'r') as file:
    lines = file.readlines()

neighbours = build_graph(lines)
print(neighbours)

paths_count = count_paths(neighbours, 'you', 'out')
print(paths_count)
