
import os
import re
from collections import deque, Counter, defaultdict


with open(f"{os.path.splitext(os.path.basename(__file__))[0]}.txt") as f:
    INPUT = f.read().splitlines()


vals = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2
}

def snafu2num(snafu: str):
    reverse = snafu[::-1]
    power = 5
    tot = 0
    for i, digit in enumerate(reverse):
        tot += (power ** (i+1)) *  vals[digit]
    return tot
print(snafu2num('1-0---0'))
        
        
        