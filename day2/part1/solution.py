with open(r'day2\part1\data.txt', 'r') as file:
    lines = file.readlines()
    line = lines[0].rstrip()
    poprawny =0
    res = 0
    ranges = line.split(',')
    for rng in ranges:
        from_,to_ = rng.split('-')
        n,m = len(from_),len(to_)
        mid = (n//2,m//2)
        if n == m and n%2 == 0:
            mid = mid[0]
            ind = -1
            for i in range(n):
                if from_[i] == to_[i]:
                    ind+=1
                else:
                    break
            half1_from,half2_from = int(from_[0:mid]),int(from_[mid:])
            half1_to,half2_to = int(to_[0:mid]),int(to_[mid:])
            # if ind == -1 :
            #     for i in range()
            if ind+1 >= mid:
                if half1_from <= half2_to and half1_from>=half2_from:
                    res += int(str(half1_from)+str(half1_from))
            else:
                sub = 0
                flag = True
                for i in range(half1_from,half1_to+1):
                    candidate = int(str(i)+str(i))
                    if candidate >= int(from_) and candidate <= int(to_):
                        sub += candidate
                res += sub
                                
        else:
            sub = 0
            frm = from_[0:mid[0]]
            if frm =='':
                frm = from_
            for i in range(int(frm),int(to_[0:mid[1]+1])):
                candidate = int(str(i)+str(i))
                if candidate >= int(from_) and candidate <= int(to_):
                    sub += candidate
            res += sub
        # for i in range(int(from_),int(to_)):
        #     if len(str(i))%2 ==0:
        #         s = str(i)
        #         mid = len(s)//2
        #         first_half,second_half = s[0:mid],s[mid:]
        #         if first_half == second_half:
        #             poprawny += i
    print(res)
                
                