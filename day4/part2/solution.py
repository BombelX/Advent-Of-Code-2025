with open (r'./day4/part1/data.txt', 'r') as file:
    lines = file.readlines()
res = 0

lines = [list(line.rstrip()) for line in lines]
moves = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]
n,m = len(lines),len(lines[0])


def fork_lift(lines):
    res = 0
    to_del = []
    for y,line in enumerate(lines):
        for x,char in enumerate(line):
            if char == '@':
                cnt = 0
                for dx,dy in moves:
                    new_x,new_y = x+dx,y+dy
                    if new_x >= 0 and new_x < n and new_y >=0 and new_y < m:
                        if lines[new_y][new_x] == '@':
                            cnt += 1
                if cnt < 4:
                    to_del.append((y,x))
                    res+=1
            else:
                continue
    for y,x in to_del:
        lines[y][x] = '.'
    if res>0:
        return fork_lift(lines)+res
    return 0
        
print(fork_lift(lines))