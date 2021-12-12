
import numpy as np

f = open('./data_11.in').read().splitlines()
grid = [[int(i) for i in x] for x in f]
R, C = len(grid), len(grid[0])

ans = 0
def flash(r,c):
    global ans
    ans += 1
    grid[r][c] = -1
    for dr in [-1,0,1]:
        for dc in [-1,0,1]:
            rr = r+dr
            cc = c+dc
            if 0<=rr<R and 0<=cc<C and grid[rr][cc]!=-1:
                grid[rr][cc] += 1
                if grid[rr][cc] >= 10:
                    flash(rr,cc)

t = 0
while True:
    t += 1
    for r in range(R):
        for c in range(C):
            grid[r][c] += 1
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 10:
                flash(r,c)
    done = True
    for r in range(R):
        for c in range(C):
            if grid[r][c] == -1:
                grid[r][c] = 0
            else:
                done = False
    if t == 100:
        print(ans)
    if done:
        print(t)
        break
