
from typing import List
import pprint

f = open('./2020_11.in').read().splitlines()
first = [['#' if i == 'L' else '.' for i in col] for col in f]


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
                        if 0 <= r+dx < len(f) and 0 <= c+dy < len(f[0]) and current[r+dx][c+dy] == '#':
                            future[r][c] = '#'
                            break
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
                    

        
        CURRENT = sum([i.count("#") for i in current])
        FUTURE = sum([i.count("#") for i in future])
        
        if CURRENT == FUTURE: 
            stop = True
        
        current = future
        
        
    return sum([i.count("#") for i in current])

    
change_seat(first)
