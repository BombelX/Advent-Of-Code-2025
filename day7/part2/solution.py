
with open(r'day7/part2/data.txt', 'r') as file:
    lines = file.readlines()


mem = {}

start = list(lines[0].strip()).index('S')
n = len(lines[0].strip())
m = len(lines)
def explore(line_index,pos):
    if (line_index,pos) in mem:
        return mem[(line_index,pos)]
    if line_index == m:
        return 1
    line = lines[line_index].strip()
    if pos >= len(line) or pos < 0:
        return 0
    x = line[pos]
    if x != '^':
        x = explore(line_index+1,pos)
        mem[(line_index,pos)] = x
        return x

    else:
        left = explore(line_index+1,pos-1)
        right = explore(line_index+1,pos+1)
        mem[(line_index,pos)] = left+right
    return left+right
time_lines = explore(1,start)
print(time_lines)