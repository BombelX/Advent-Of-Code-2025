from collections import defaultdict
import functools
import sys

sys.setrecursionlimit(10000)

def build_graph(lines):
    graph = defaultdict(list)
    for raw in lines:
        if not raw.strip():
            continue
        parts = raw.split(':', 1)
        if len(parts) != 2: continue # 
        left, right = parts
        node = left.strip()
        targets = right.strip()
        if targets:
            graph[node].extend(targets.split())
    return graph

def count_paths(graph, start, target):
    @functools.cache
    def dfs(node, fft_meeted, dac_meeted):
        if node == 'fft':
            fft_meeted = True
        if node == 'dac':
            dac_meeted = True
        if node == target:
            return 1 if fft_meeted and dac_meeted else 0
        total = 0
        for neighbor in graph[node]:
            total += dfs(neighbor, fft_meeted, dac_meeted)
        return total
    return dfs(start, start == 'fft', start == 'dac')

try:
    with open('day11/part2/data.txt', 'r') as file:
        lines = file.readlines()
    neighbours = build_graph(lines)
    import time
    start_time = time.time()
    paths_count = count_paths(neighbours, 'svr', 'out')
    end_time = time.time()
    print(f"Liczba ścieżek: {paths_count}")
    print(f"Czas obliczeń: {end_time - start_time:.4f} sekundy")

except FileNotFoundError:
    print("Nie znaleziono pliku. Upewnij się co do ścieżki.")