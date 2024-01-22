
import os
import re
from collections import defaultdict


with open(os.path.join(os.path.dirname(__file__), f"{os.path.splitext(__file__)[0]}.in")) as f:
# with open(os.path.join(os.path.dirname(__file__), f"{os.path.splitext(__file__)[0]}.test")) as f:
    q = f.readlines()

#* Question 1
a1 = 0

for line in q:
    win, owned = line.split('|')
    win = win[win.index(':'):]
    
    win_nums = re.findall('\d{1,2}', win)
    owned_nums = re.findall('\d{1,2}', owned)
    
    current_points = 0
    for _ in range(len([i for i in win_nums if i in owned_nums])):
        if current_points == 0:
            current_points = 1
        else:
            current_points *= 2
    
    a1 += current_points
    
print(f"Answer 1: {a1}")


#* Question 2
copies = defaultdict(int,{ k+1: 0 for k in range(len(q)) })
for i, line in enumerate(q):
    copies[i + 1] += 1
    win, owned = line.split('|')
    win = win[win.index(':'):]
    
    win_nums = re.findall('\d{1,2}', win)
    owned_nums = re.findall('\d{1,2}', owned)
    
    wins = len([i for i in win_nums if i in owned_nums])
    
    for _ in range(copies.get(i + 1)):
        for n in range(wins):
            if i + n + 2 not in copies.keys():
                break
            copies[i + n + 2] += 1

a2 = sum(copies.values())
print(f"Answer 2: {a2}")