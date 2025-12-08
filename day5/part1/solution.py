with open (r'./day5/part1/data.txt', 'r') as file:
    lines = file.readlines()

flag = True
ranges = []
ids = []

for line in lines:
    if line == '\n':
        flag = False
        continue
    line = line.rstrip()
    if flag:
        line = line.split('-')
        ranges.append((int(line[0]),int(line[1])))
    else:
        ids.append(int(line))
ranges.sort(key = lambda x:x[0])
marged_rangess = []
start = ranges[0][0]
tmp_end = ranges[0][1]
i = 1
while start < ranges[-1][0] and i<len(ranges):
    if ranges[i][0] <= tmp_end:
        tmp_end = max(ranges[i][1],tmp_end)
    else:
        new_rn = (start,tmp_end)
        marged_rangess.append(new_rn)
        start = ranges[i][0]
        tmp_end = ranges[i][1]
    i+=1
new_rn = (start,tmp_end)
marged_rangess.append(new_rn)


def is_in_range(rng,x):
    if x>=rng[0] and x<=rng[1]:
        return True
    else :
        return False
    
print(marged_rangess)
n = len(marged_rangess)
def bin_search(start=0,end=n,target=0):
    if start>end or end<start:
        return False
    mid = (start+end)//2
    if mid >= n :
        return False
    if is_in_range(marged_rangess[mid],target): 
        return True
    elif target<marged_rangess[mid][0]:
        return bin_search(start,mid-1,target)
    else:
        return bin_search(mid+1,end,target)

res = 0
for id in ids:
    if bin_search(target=id):
        res+=1

print(res)


