
import os
import re
from collections import deque

# with open(os.path.join(os.path.dirname(__file__), f"{os.path.splitext(__file__)[0]}.in")) as f:
with open(os.path.join(os.path.dirname(__file__), f"{os.path.splitext(__file__)[0]}.test")) as f:
    q = f.read()

cats = q.split('\n\n')

seeds, s2s, s2f, f2w, w2l, l2t, t2h, h2l = mod_cat = [
    i.split('\n')[1:] for i in cats
]

seeds = list(map(int, mod_cat[0][0].split(' ')))
s2s, s2f, f2w, w2l, l2t, t2h, h2l = ( 
    list(map(lambda s: list(map(int, s.split(' '))), i)) for i in mod_cat[1:]
)

for a, b, c in s2s:
    range(b, c)
    




# #* Question 1
# a1 = 0


# print(f"Answer 1: {a1}")


# #* Question 2
# a2 = 0


# print(f"Answer 2: {a2}")