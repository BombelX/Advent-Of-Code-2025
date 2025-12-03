def is_invalid_id(n):
    s = str(n)
    length = len(s)
    for d in range(1, length): 
        if length % d != 0:
            continue  
        block = s[:d]
        if block * (length // d) == s:
            return True
    return False
total_sum = 0

with open('./day2/part2/data.txt', 'r') as file:
    lines = file.readline().split(',')

for line in lines:
    start, end = line.strip().split('-')
    start, end = int(start), int(end)
    for x in range(start, end + 1):
        if is_invalid_id(x):
            total_sum += x
print(total_sum)
#bruteforce