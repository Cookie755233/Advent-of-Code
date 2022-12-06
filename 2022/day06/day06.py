import os
import re
from collections import deque, Counter


with open(f"{os.path.splitext(os.path.basename(__file__))[0]}.txt") as f:
    INPUT = f.read().splitlines()[0]
leng = len(INPUT)

def solve1(p2=False, leng=leng):
    ans=None
    unique_cnt = 4 if not p2 else 14
    for i, _ in enumerate(INPUT):
        while i+unique_cnt <= leng and not ans:
            
            if len(set(INPUT[i:i+unique_cnt])) == len(INPUT[i:i+unique_cnt]):
                ans = i+unique_cnt
                break
            else:
                break
    return ans

print(f'The Answer in Part 1 is : {solve1(p2=False)}')
print(f'The Answer in Part 2 is : {solve1(p2=True)}')
                