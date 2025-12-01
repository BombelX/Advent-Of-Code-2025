with open(r'day1\part1\data.txt', 'r') as file:
    lines = file.readlines()
    counter = 0
    dial = 50
    for line in lines:
        line = line.rstrip()
        direction,rotation = line[0],int(line[1::])
        if direction == 'R':
            dial = (dial+rotation)%100
        else:
            rotation = rotation%100
            dial -= rotation
            if dial < 0:
                dial += 100
        if dial == 0:
            counter +=1
print(counter)