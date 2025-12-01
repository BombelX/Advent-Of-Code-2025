with open(r'day1\part2\data.txt', 'r') as file:
    lines = file.readlines()
    counter = 0
    dial = 50
    for line in lines:
        flag = False
        old_dial = dial
        line = line.rstrip()
        direction,rotation = line[0],int(line[1::])
        counter += rotation//100
        rotation = rotation%100
        if direction == 'R':
            dial += rotation
            if dial > 99:
                dial %= 100
                flag = True
        else:
            dial -= rotation
            if dial < 0:
                dial += 100
                flag = True
        if dial == 0 or (flag and old_dial!=0):
            counter +=1
print(counter)