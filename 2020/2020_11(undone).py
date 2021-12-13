
from typing import List
import pprint

# f = open('./2020_11.in').read().splitlines()
# first = [['#' if i == 'L' else '.' for i in col] for col in f]
first = '''#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##'''
f = [[str(i) for i in x] for x in first.splitlines()]
def change_seat(f: List[List]) -> int:
    '''
    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    If a seat is occupied (#) and 4 or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.
    
    Simulate your seating area by applying the seating rules repeatedly until no seats change state.
    How many seats end up OCCUPIED?
    '''
    current = f.copy()
    stop = False
    
    while not stop:
        future = [['' for _ in range(len(f[0]))] for _ in range(len(f))]
        for r in range(len(f)):
            for c in range(len(f[0])):
                dx = [1, 1, 1, 0, 0, -1, -1, -1]
                dy = [1, 0, -1, 1, -1, 1, 0, -1]

                # empty
                if current[r][c] == 'L':
                    for dx, dy in zip(dx, dy):
                        if 0 <= r+dx < len(f) and 0 <= c+dy < len(f[0]):
                            if all([current[r+dx][c+dy] in ['L', '.']]):
                                future[r][c] = '#'
                            else:
                                future[r][c] = 'L'
                                


                # occupied
                elif current[r][c] == '#':
                    s = 0
                    for dx, dy in zip(dx, dy):
                        if 0 <= r+dx < len(f) and 0 <= c+dy < len(f[0]):         
                            s += current[r+dx][c+dy] == '#' 
                    if s >= 4:
                        future[r][c] = 'L'
                    else: 
                        future[r][c] = '#'

                else: 
                    future[r][c] = '.'

        pprint.pprint(future)
        CURRENT = sum([i.count("#") for i in current])
        FUTURE = sum([i.count("#") for i in future])
        
        if CURRENT == FUTURE: 
            stop = True
        
        current = future
        
        
    return sum([i.count("#") for i in current])

    
print(change_seat(f))


# Alternatives

from copy import deepcopy

L = [list(l.strip()) for l in f]
R = len(L)
C = len(L[0])

def solve(L, p1):
    t = 0
    while True:
        t += 1

        newL = deepcopy(L)
        change = False
        for r in range(R): 
            for c in range(C):
                nocc = 0
                for dr in [-1,0,1]:
                    for dc in [-1,0,1]:
                        if not (dr==0 and dc==0):
                            rr = r+dr
                            cc = c+dc
                            # Only skip floor in part 2
                            while 0<=rr<R and 0<=cc<C and L[rr][cc]=='.' and (not p1):
                                rr = rr+dr
                                cc = cc+dc
                            if 0<=rr<R and 0<=cc<C and L[rr][cc]=='#':
                                nocc += 1

                if L[r][c]=='L':
                    if nocc == 0:
                        newL[r][c] = '#'
                        change = True
                # Threshold changes from 4->5 in part 2
                elif L[r][c] == '#' and nocc>=(4 if p1 else 5):
                    newL[r][c] = 'L'
                    change = True
        if not change:
            break
        L = deepcopy(newL)

    ans = 0
    for r in range(R):
        for c in range(C):
            if L[r][c] == '#':
                ans += 1
    return ans

print(solve(L, True))
print(solve(L, False))
