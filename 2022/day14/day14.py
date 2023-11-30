
import os
import re
from collections import deque, Counter, defaultdict

with open(f"{os.path.splitext(os.path.basename(__file__))[0]}.txt") as f:
    INPUT = f.read().splitlines()

R = set()
for line in INPUT:
    prev = None
    for point in line.split('->'):
        x,y = point.split(',')
        x,y = int(x),int(y)
        if prev is not None:
            dx = x-prev[0]
            dy = y-prev[1]
            len_ = max(abs(dx),abs(dy))
            for i in range(len_+1):
                xx = prev[0]+i*(1 if dx>0 else (-1 if dx<0 else 0))
                yy = prev[1]+i*(1 if dy>0 else (-1 if dy<0 else 0))
                R.add((xx,yy))
        prev = (x,y)

floor = 2+max(r[1] for r in R)
print(floor)