import math
from collections import defaultdict
import time
class UnionFind3D:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.size = {}  

    def add(self, point):
        if point not in self.parent:
            self.parent[point] = point
            self.rank[point] = 0
            self.size[point] = 1 

    def find(self, point):
        if self.parent[point] != point:
            self.parent[point] = self.find(self.parent[point])
        return self.parent[point]

    def union(self, p1, p2):
        root1 = self.find(p1)
        root2 = self.find(p2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
                self.size[root1] += self.size[root2]  
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
                self.size[root2] += self.size[root1]  
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
                self.size[root1] += self.size[root2]  
            return True
        return False

    def get_size(self, point):
        root = self.find(point)
        return self.size[root]


def get_all_structures(uf, all_points):
    structures = defaultdict(list)
    
    for point in all_points:
        root = uf.find(point)
        structures[root].append(point)
        
    return structures
def kruskal(verticles,limit):
    uf = UnionFind3D()
    for point in verticles:
            uf.add(point)

    edges = []
    n = len(verticles)
    for i in range(n):
        for j in range(i + 1, n):
            p1 = verticles[i]
            p2 = verticles[j]
            dist = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2
            edges.append((p1, p2, dist))
    edges.sort(key=lambda x: x[2])
    last_p1,last_p2 = None,None
    cost = 0
    count = 0
    for p1,p2,w in edges:
        if uf.find(p1) != uf.find(p2):
            uf.union(p1,p2)
            last_p1,last_p2 = p1,p2
            cost += w
            count += 1
            if count == len(verticles)-1:
                break
    cl = get_all_structures(uf, verticles)
    return cl,last_p1[0]*last_p2[0]



def read_file(path):
    with open(path,'r') as file:
        lines = file.readlines()
        
    verticles = []
    for line in lines:
        line = line.strip().split(',')
        verticles.append((int(line[0]), int(line[1]), int(line[2])))
    return verticles
def solution(path):
    time_start = time.time()
    verticles = read_file(path)
    clusters, product = kruskal(verticles,1000)
    print("Time taken:", time.time() - time_start)
    return product
    
    # maxes=[1,1,1]
    
    # for _, points in clusters.items():
    #     n = len(points)
    #     if n> maxes[0]:
    #         maxes[2] = maxes[1]
    #         maxes[1] = maxes[0]
    #         maxes[0] = n
    #     elif n > maxes[1]:
    #         maxes[2] = maxes[1]
    #         maxes[1] = n
    #     elif n > maxes[2]:
    #         maxes[2] = n
    # print(maxes)
    # return maxes[0]*maxes[1]*maxes[2]
print(solution('day8_pc/part1/data.txt'))