
import re

f = open('./data_22.in').read().splitlines()

# cube = [[[0 for _ in range(-50, 51)] for _ in range(-50, 51)] for _ in range(-50, 51)]

# for line in f:
#     x = line.split()
#     turn = x[0]
#     mx, MX, my, MY, mz, MZ = [int(i) for i in re.findall(r'(-?\d+)', x[1])]
#     if not all([-50<i<50 for i in [mx, MX, my, MY, mz, MZ]]): 
#         continue
#     for x in range(mz, MZ+1):
#         for y in range(my, MY+1):
#             for z in range(mx, MX+1):
#                 if turn == 'on':
#                     cube[x][y][z] = 1
#                 else:
#                     assert turn == 'off'
#                     cube[x][y][z] = 0

# print(
#     sum( [sum([sum(i) for i in x]) for x in cube] ))


from collections import deque

f = open('./data_22.in').read().splitlines()


# def insert(l, x0, x1):
#     for a, b in l:
#         if b < x0: l.appendright((x0, x1))
#         elif x1 < a: l.appendleft((x0, x1))
#     else:
        


x = y = z = deque([])
for line in f:
    x = line.split()
    turn = x[0]
    x0, x1, y0, y1, z0, z1 = [int(i) for i in re.findall(r'(-?\d+)', x[1])]
    if not x:
        x.append(x0, x1)
        y.append(y0, y1)
        z.append(z0, z1)
    else:
        if 


# Part 2
# from collections import defaultdict

# with open("./data_22.in") as fin:
#     raw_data = fin.read().strip().split("\n")

# steps = []


# def volume(bounds):
#     # Compute volume of cube
#     p = 1
#     for b in bounds:
#         assert b[1] >= b[0]
#         p *= abs(b[1] - b[0]) + 1
#     return p


# def overlap(bounds1, bounds2):
#     # Intersect two cubes to find a new cube!
#     ans = []
#     for b1, b2 in zip(bounds1, bounds2):
#         if b1[1] < b2[0] or b2[1] < b1[0]:
#             return None

#         bounds = (max(b1[0], b2[0]), min(b1[1], b2[1]))
#         ans.append(bounds)

#     return tuple(ans)


# for line in raw_data:
#     parts = line.split(" ")
#     switch = parts[0] == "on"
#     bounds = []
#     for axis in parts[1].split(","):
#         axis = axis.split("..")
#         bounds.append((int(axis[0][2:]), int(axis[1])))

#     steps.append((switch, tuple(bounds)))


# counts = defaultdict(int)
# for i in range(len(steps)):
#     switch, bounds = steps[i]

#     new_counts = defaultdict(int)
#     keys = set(counts.keys())
#     for o_cube in keys:
#         o_switch = counts[o_cube] > 0
#         o = overlap(bounds, o_cube)
#         if o == None:
#             continue

#         new_counts[o] -= counts[o_cube]  # Reset to 0

#     if switch:
#         new_counts[bounds] += 1

#     for c in new_counts:
#         counts[c] += new_counts[c]


# ans = 0
# for cube in counts:
#     ans += volume(cube) * counts[cube]
    
# print(ans)
            