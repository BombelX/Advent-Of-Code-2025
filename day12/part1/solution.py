with open('day12/part1/data.txt','r') as file:
    lines = file.readlines()


boxes = [[[0,1,1],[1,1,0],[1,1,1]],
         [[1,1,0],[1,1,0],[1,1,1]],
         [[1,1,1],[1,0,0],[1,1,1]],
         [[1,1,0],[0,1,1],[0,0,1]],
         [[1,0,0],[1,1,1],[1,1,1]],
         [[1,1,1],[0,1,0],[1,1,1]]]


boxes = [[[1,1,1],[1,1,0],[1,1,0]],
         [[1,1,1],[1,1,0],[0,1,1]],
         [[0,1,1],[1,1,1],[1,1,0]],
         [[1,1,0],[1,1,1],[1,1,0]],
         [[1,1,1],[1,0,0],[1,1,1]],
         [[1,1,1],[0,1,0],[1,1,1]]]

box_elems = [7,7,7,5,6,7]

def rotate_box_90(box):
    rows = len(box)
    cols = len(box[0])
    rotated = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            rotated[j][rows - 1 - i] = box[i][j]
    return rotated

def get_all_rotations(box):
    rotations = [box]
    current = box
    for _ in range(3):
        current = rotate_box_90(current)
        if current not in rotations:
            rotations.append(current)
    return rotations

def can_place_box(area, width, height, box, start_pos):
    row = start_pos // width
    col = start_pos % width
    
    for i, line in enumerate(box):
        for j, cell in enumerate(line):
            if cell == 1:
                new_row = row + i
                new_col = col + j
                if new_row >= height or new_col >= width:
                    return False
                if area[new_row * width + new_col] != 0:
                    return False
    return True

def place_box(area, width, height, box, start_pos, mark):
    row = start_pos // width
    col = start_pos % width
    
    for i, line in enumerate(box):
        for j, cell in enumerate(line):
            if cell == 1:
                new_row = row + i
                new_col = col + j
                if 0 <= new_row < height and 0 <= new_col < width:
                    area[new_row * width + new_col] = mark

def is_possible(box_index, dimension):
    width = int(dimension[0])
    height = int(dimension[1])
    area = [0] * (width * height)
    
    boxes_to_place = []
    for i, count in enumerate(box_index):
        for _ in range(int(count)):
            boxes_to_place.append(get_all_rotations(boxes[i]))
    
    def backtrack(idx):
        if idx == len(boxes_to_place):
            return True
        
        box_rotations = boxes_to_place[idx]
        
        for pos in range(width * height):
            for rotation in box_rotations:
                if can_place_box(area, width, height, rotation, pos):
                    place_box(area, width, height, rotation, pos, 1)
                    if backtrack(idx + 1):
                        return True
                    place_box(area, width, height, rotation, pos, 0)
        
        return False
    
    return backtrack(0)


def solve(boxes, lines):
    print("Starting to solve the problems...")
    res = 0
    for problem in lines:
        print(f"Processing problem: {problem.strip()}")
        dimension, box_index = problem.split(":")[0].split('x') , problem.split(":")[1].strip().split(' ')
        # print(dimension, box_index)
        area = int(dimension[0]) * int(dimension[1])
        min_needed_arena = 0
        for i,index in enumerate(box_index):
            min_needed_arena += box_elems[i]*int(index)
        if min_needed_arena <= area:
            if is_possible(box_index, dimension):
                res +=1
                print(f"Possible for {problem.strip()}")
            else:
                print(f"Not possible for {problem.strip()}")
        else:
            print(f"Not possible for {problem.strip()}")
    return res    

result = solve(boxes, lines)
print(f"Solution: {result}")