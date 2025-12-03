with open (r'./day3/part2/data.txt', 'r') as file:
    lines = file.readlines()
res = 0
for line in lines :
    line = line.rstrip()
    sub = 0
    tab = [0]*12
    n = len(line)
    for i in range(n):
        start = 0
        if n-i<12:
            start = 12-n+i
        flag = False
        for j in range(start,12):
            if flag:
                if tab[j] == 0:
                    break
                tab[j] = 0
                continue
            num = int(line[i])
            if tab[j]<num:
                tab[j] = num
                flag = True
    for i in range(12):
        sub+=tab[i]*10**(11-i)
    print(sub)
    res+=sub
print(res)