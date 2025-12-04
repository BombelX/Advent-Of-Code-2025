with open (r'./day3/part1/data.txt', 'r') as file:
    lines = file.readlines()
res = 0
for line in lines:
    line = line.rstrip()
    max_d,max_j = 0,0
    for number in line[:-1]:
        if int(number) > max_d:
            max_d = int(number)
            max_j = 0
        elif int(number) > max_j:
            max_j = int(number)
    max_j = max(max_j,int(line[-1]))
    sub = max_d*10+max_j
    # print(sub)
    res+=sub
print(res)