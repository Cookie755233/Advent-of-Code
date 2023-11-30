
import os
import re
from collections import deque, Counter, defaultdict
import ast

with open(f"{os.path.splitext(os.path.basename(__file__))[0]}.txt") as f:
    INPUT = f.read()

tmp = '''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]'''

# pairs = INPUT.split('\n\n')
tot = 0
pairs = tmp.split('\n\n')

def get_val(x):
    if isinstance(x, int):
        return x
    if isinstance(x, list):
        for i in x:
            return get_val(i)

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a > b
    else:
        
        for x, y in zip(a, b):


for i, pair in enumerate(pairs):
    A, B = pair.splitlines()
    A = ast.literal_eval(A)
    B = ast.literal_eval(B)
    if len(B) > len(A): 
        continue
    for a, b in zip(A, B):
        val_a, val_b = get_val(a), get_val(b)
        # print(f'a:{a}, val_a:{val_a}')
        # print(f'b:{b}, val_b:{val_b}')
        if val_a is None and val_b is None: continue
        if val_a > val_b: break
    
    print(i+1)
    tot += i+1
    print()
        
print(tot)
