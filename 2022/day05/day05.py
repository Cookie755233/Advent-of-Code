import os
from collections import deque
import re


with open(f"{os.path.splitext(os.path.basename(__file__))[0]}.txt") as f:
    INPUT = f.read().splitlines()

'''
[G]                 [D] [R]        
[W]         [V]     [C] [T] [M]    
[L]         [P] [Z] [Q] [F] [V]    
[J]         [S] [D] [J] [M] [T] [V]
[B]     [M] [H] [L] [Z] [J] [B] [S]
[R] [C] [T] [C] [T] [R] [D] [R] [D]
[T] [W] [Z] [T] [P] [B] [B] [H] [P]
[D] [S] [R] [D] [G] [F] [S] [L] [Q]
 1   2   3   4   5   6   7   8   9 
'''

CRATES = {
    1: deque(['G', 'W', 'L', 'J', 'B', 'R', 'T', 'D']),
    2: deque(['C', 'W', 'S']),
    3: deque(["M", "T", "Z", "R"]),
    4: deque(["V", "P", 'S', 'H', 'C', "T", 'D']),
    5: deque(['Z', "D", 'L', 'T', 'P', 'G']),
    6: deque(['D', 'C', 'Q', 'J', 'Z', 'R', 'B', 'F']),
    7: deque(['R', 'T', 'F', 'M', 'J', 'D', 'B', 'S']),
    8: deque(['M', 'V', 'T', 'B', 'R', 'H', 'L']),
    9: deque(['V', 'S', 'D', 'P', 'Q']),
}


def solve(part, crates):
    for line in INPUT:
        a, b, c = [int(i) for i in re.findall(
            r'move (\d+) from (\d+) to (\d+)', line)[0]]
    if part == 'A':
        for _ in range(a):
            x = crates[b].popleft()
            crates[c].appendleft(x)
    if part == 'B':
        remain, out = list(crates[b])[:a], list(crates[b])[a:]
        crates[c] = out + list(crates[c])
        crates[b] = remain

    return ''.join([crates[i][0] for i in range(1, 10)])


print(f"The Answer in Part 1 is : {solve(part='A', crates=CRATES)}")
print(f"The Answer in Part 1 is : {solve(part='B', crates=CRATES)}")
