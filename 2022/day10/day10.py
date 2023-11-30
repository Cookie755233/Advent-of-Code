
import os
import re
from collections import deque, Counter, defaultdict
from pprint import pprint as pp


with open(f"{os.path.splitext(os.path.basename(__file__))[0]}.txt") as f:
    INPUT = f.read().splitlines()


'''Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six signal strengths?
'''
# INPUT = '''addx 15
# addx -11
# addx 6
# addx -3
# addx 5
# addx -1
# addx -8
# addx 13
# addx 4
# noop
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx -35
# addx 1
# addx 24
# addx -19
# addx 1
# addx 16
# addx -11
# noop
# noop
# addx 21
# addx -15
# noop
# noop
# addx -3
# addx 9
# addx 1
# addx -3
# addx 8
# addx 1
# addx 5
# noop
# noop
# noop
# noop
# noop
# addx -36
# noop
# addx 1
# addx 7
# noop
# noop
# noop
# addx 2
# addx 6
# noop
# noop
# noop
# noop
# noop
# addx 1
# noop
# noop
# addx 7
# addx 1
# noop
# addx -13
# addx 13
# addx 7
# noop
# addx 1
# addx -33
# noop
# noop
# noop
# addx 2
# noop
# noop
# noop
# addx 8
# noop
# addx -1
# addx 2
# addx 1
# noop
# addx 17
# addx -9
# addx 1
# addx 1
# addx -3
# addx 11
# noop
# noop
# addx 1
# noop
# addx 1
# noop
# noop
# addx -13
# addx -19
# addx 1
# addx 3
# addx 26
# addx -30
# addx 12
# addx -1
# addx 3
# addx 1
# noop
# noop
# noop
# addx -9
# addx 18
# addx 1
# addx 2
# noop
# noop
# addx 9
# noop
# noop
# noop
# addx -1
# addx 2
# addx -37
# addx 1
# addx 3
# noop
# addx 15
# addx -21
# addx 22
# addx -6
# addx 1
# noop
# addx 2
# addx 1
# noop
# addx -10
# noop
# noop
# addx 20
# addx 1
# addx 2
# addx 2
# addx -6
# addx -11
# noop
# noop
# noop'''.splitlines()


BORAD = [[],[],[],[],[],[]]

def check20(cycle, curr_val):
    if cycle in (20, 60, 100, 140, 180, 220):
        return curr_val * cycle
    return 0

def draw(cycle, lit):
    x = (cycle-1)//40
    sig = '#' if lit else '.'
    
    BORAD[x].append(sig)

# curr_val = 1
# cycle = 0
# tot = 0
# for i, line in enumerate(INPUT):
#     if line == 'noop':
#         cycle += 1
#         tot += check20(cycle, curr_val)
#     else:
#         sig, val = line.split()
#         cycle += 1
#         tot += check20(cycle, curr_val)
#         cycle += 1
#         tot += check20(cycle, curr_val)
#         curr_val += int(val)

# print(tot)


curr_val = 1
cycle = 0
for i, line in enumerate(INPUT):
    if line == 'noop':
        cycle += 1
        draw(cycle, curr_val-1<=(cycle-1)%40<=curr_val+1)
        print(f'drawed: {"".join(BORAD[(cycle-1)//40])}')
        
    else:
        sig, val = line.split()
        cycle += 1
        print(f'cycle: {cycle} -- {line}')
        draw(cycle, curr_val-1<=(cycle-1)%40<=curr_val+1)
        print(f'drawed: {"".join(BORAD[(cycle-1)//40])}')
        cycle += 1
        print(f'cycle: {cycle} -- {line}')
        draw(cycle, curr_val-1<=(cycle-1)%40<=curr_val+1)
        print(f'drawed: {"".join(BORAD[(cycle-1)//40])}')
        curr_val += int(val)
        print(f'cycle: {cycle} -- add val {val}, curr = {curr_val}')

print( '\n'.join([''.join(b) for b in BORAD]) )