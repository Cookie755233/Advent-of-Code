
from itertools import permutations
from collections import defaultdict



f = open('./data_19.in').read()
f ='''--- scanner 0 ---
-1,-1,1
-2,-2,2
-3,-3,3
-2,-3,1
5,6,-4
8,0,7

--- scanner 0 ---
1,-1,1
2,-2,2
3,-3,3
2,-1,3
-5,4,-6
-8,-7,0

--- scanner 0 ---
-1,-1,-1
-2,-2,-2
-3,-3,-3
-1,-3,-2
4,6,5
-7,0,8

--- scanner 0 ---
1,1,-1
2,2,-2
3,3,-3
1,3,-2
-4,-6,5
7,0,8

--- scanner 0 ---
1,1,1
2,2,2
3,3,3
3,1,2
-6,-4,-5
0,7,-8
9,9,9'''



datasets = [i.splitlines()[1:] for i in f.split('\n\n') ]
D = defaultdict(int)
P = defaultdict(int)
for i in range(500):
    P[sum([j for j in range(i)])] = i

tot = 0
for data in datasets:
    l = len(data)
    
    # permutaions and see (0,1)/(1,0) as one
    perms = permutations([i for i in range(l)], 2)
    perms = list(set(tuple(sorted(l)) for l in perms))
    tot += len(perms)
    

    for a, b in perms:
        x1, y1, z1 = [int(i) for i in data[a].split(',')]
        x2, y2, z2 = [int(i) for i in data[b].split(',')]
        dx, dy, dz = abs(x2-x1), abs(y2-y1), abs(z2-z1)
        for pd in permutations([dx, dy, dz]):
            if pd in D.keys():
                D[pd] += 1
                break
        else:
            D[(dx, dy, dz)] += 1
# print(tot, len(D), tot-len(D))
print(len(D))
print(D.values())