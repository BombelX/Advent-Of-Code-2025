from collections import defaultdict
from copy import copy

with open(r'day7/part1/data.txt', 'r') as file:
    lines = file.readlines()


beam = defaultdict(bool)

beam[list(lines[0].strip()).index('S')] = True
spliters_cnt = 0
n = len(lines[0].strip())
for line in lines:
    line = list(line.strip())
    iter = list(beam.keys())
    for b in iter:
        if beam[b] and line[b] == '^':
            spliters_cnt += 1
            beam[b] = False
            if b - 1 >= 0:
                beam[b - 1] = True
            if b + 1 < n:
                beam[b + 1] = True
print(spliters_cnt)