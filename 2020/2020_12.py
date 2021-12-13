'''
Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is currently facing.

The ship starts by facing east.

At the end of these instructions, the ship's Manhattan distance (sum of the absolute values of its east/west position and its north/south position) from its starting position is 17 + 8 = 25. ( east 17, south 8 )
'''

from collections import deque
# test = '''F10
# N3
# F7
# R90
# F11'''

f = open('./2020_12.in').read().splitlines()

# Part I
directions = deque(['E','S','W','N'])
pos = deque([0, 0, 0, 0])

for ins in f:
    act, val = ins[0], int(ins[1:])
    
    if act in directions:
        pos[directions.index(act)] += val
    
    elif act == 'L':
        pos.rotate(val//90)
        directions.rotate(val//90)
    elif act == 'R':
        pos.rotate(-val//90)
        directions.rotate(-val//90)
        
    else:
        pos[0] += val

    # print(pos)
print(abs(pos[0] - pos[2]) + abs(pos[1] - pos[3]))

'''
Almost all of the actions indicate how to move a waypoint which is relative to the ship's position:

Action N means to move the waypoint north by the given value.
Action S means to move the waypoint south by the given value.
Action E means to move the waypoint east by the given value.
Action W means to move the waypoint west by the given value.
Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
Action F means to move forward to the waypoint a number of times equal to the given value.
The waypoint starts 10 units east and 1 unit north relative to the ship. The waypoint is relative to the ship; that is, if the ship moves, the waypoint moves with it.

The waypoint starts 10 units east and 1 unit north relative to the ship.
'''


# Part II
import numpy as np

waypoint = deque([10, 0, 0, 1])
directions = deque(['E','S','W','N'])
pos = np.zeros(4)
for ins in f:
    act, val = ins[0], int(ins[1:])
    
    if act in directions:
        waypoint[directions.index(act)] += val
        
    
    elif act == 'L':
        waypoint.rotate(-val//90)
    elif act == 'R':
        waypoint.rotate(val//90)
        
    else:
        pos += np.array(waypoint)*val
    
    # print(directions)
    # print(f'pos: {pos}')
    # print(f'waypoint: {waypoint}')
print(abs(pos[0] - pos[2]) + abs(pos[1] - pos[3]))



# Why (x,y) vs. (r,c)?
# Here we're on a plane instead of a grid, so (x,y) is a better coordinate system (more "mathy").
# What is the difference between a grid and a plane? If you're indexing into an array, it's a grid.
# The main difference is that y increases as it goes up, whereas r decreases as it goes up.

# L = [l.strip() for l in f]
# def solve_p1():
#     # Direction is a number 0,1,2,3
#     # 0=north, 1=east, 2=south, 3=west
#     DX = [0,1,0,-1]
#     DY = [1,0,-1,0]
#     x = 0
#     y = 0
#     dir_ = 1
#     for line in L:
#         cmd = line[0]
#         n = int(line[1:])
#         if cmd == 'N':
#             y += n
#         elif cmd == 'S':
#             y -= n
#         elif cmd == 'E':
#             x += n
#         elif cmd == 'W':
#             x -= n
#         elif cmd == 'L':
#             for _ in range(n//90):
#                 dir_ = (dir_+3)%4
#         elif cmd == 'R':
#             for _ in range(n//90):
#                 dir_ = (dir_+1)%4
#         elif cmd == 'F':
#             x += DX[dir_]*n
#             y += DY[dir_]*n
#         else:
#             assert False
#         print(x, y)
#     return abs(x)+abs(y)

# def solve_p2():
#     wx = 10
#     wy = 1
#     x = 0
#     y = 0
#     for line in L:
#         cmd = line[0]
#         n = int(line[1:])
#         if cmd == 'N':
#             wy += n
#         elif cmd == 'S':
#             wy -= n
#         elif cmd == 'E':
#             wx += n
#         elif cmd == 'W':
#             wx -= n
#         # Complex numbers are a good way to think about rotations!
#         # Think of the point (x,y) as the complex number x+iy
#         # Remember i^2=-1. Multiplying by i is the same as rotating 90 degrees.
#         # Why? Note i^4 = (-1)^2 = 1, so multiplying by i four times does nothing.
#         # i^2 = -1, so multiplying by i flips you around the x and y axes (which is a 180-degree rotation).
#         # (x,y)*i = (x+iy)*i = ix+i^2y = -y+ix = (-y,x)
#         # (x,y)*i^3 = (x+iy)*i^3 = i^3x+i^4y = y - ix = (y,-x)
#         elif cmd == 'L':
#             for _ in range(n//90):
#                 wx,wy = -wy,wx
#         elif cmd == 'R':
#             for _ in range(n//90):
#                 wx,wy = wy,-wx
#         elif cmd == 'F':
#             x += n*wx
#             y += n*wy
#         else:
#             assert False
#     return abs(x)+abs(y)


# print(solve_p1())
# print(solve_p2())
