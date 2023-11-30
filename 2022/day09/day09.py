
import os
from collections import deque, Counter, defaultdict
import numpy as np

with open(f"{os.path.splitext(os.path.basename(__file__))[0]}.txt") as f:
    INPUT = f.read().splitlines()

tmp ='''
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''


head, tail = np.array([0, 0]), np.array([0, 0])
MOVES = {
    'R': np.array([ 1,  0]),
    'L': np.array([-1,  0]),
    'U': np.array([ 0,  1]),
    'D': np.array([ 0, -1])
}


p1 = []
# for idx, line in enumerate(tmp.splitlines()[1:]):
for idx, line in enumerate(INPUT):
    dir_, steps = line.split()
    for i in range(int(steps)):
        head += MOVES[dir_]
        dist = head-tail
        if all([-2<i<2 for i in dist]):
            pass
        else:
            new_dist = head-tail
            if not all([-2<i<2 for i in new_dist]):
                if dir_ == 'R' or dir_ =='L':
                    tail[1] = head[1]
                else:
                    tail[0] = head[0]
            tail += MOVES[dir_]
        
        p1.append((tuple(tail)))
            


def solve():
    front, end = np.array([0, 0]), np.array([0, 0])
    seq = end
    for i, line in enumerate(tmp.splitlines()[1:3]):
        instruction, steps = line.split()
        for j in range(int(steps)):
            front += MOVES[instruction]
            for k in range(9):
                print(f'step{i}-{j}-{k}')
                seq = get_tail(front, end, instruction)
                print(f'none: {seq}')
                if list(seq) == list(end): 
                    break
        end = seq
    return end

def get_tail(front, tail, instruction):
    dist = front - tail
    if all([-2<i<2 for i in dist]):
        return tail
    else:
        if instruction == 'R' or instruction =='L':
            tail[1] = head[1]
        else:
            tail[0] = head[0]
        tail += MOVES[instruction]
        
        return tail

    

def move(head, tail, steps, instruction):
    for _ in range(steps):
        head += MOVES[instruction]
        dist = head - tail
        if all([-2<i<2 for i in dist]):
            return head, tail
        else:
            new_dist = head - tail
            if not all([-2<i<2 for i in new_dist]):
                if instruction == 'R' or instruction =='L':
                    tail[1] = head[1]
                else:
                    tail[0] = head[0]
            tail += MOVES[instruction]
            
            return head, tail


solve()




# print(f'The Answer in Part 1 is : {len(set(p1))}')
# print(f'The Answer in Part 2 is : {p2}')
                