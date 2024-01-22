
import os
import re


with open(os.path.join(os.path.dirname(__file__), 
                       f"{os.path.splitext(__file__)[0]}.in")) as f:
    q = f.readlines()


#* Question 1
a1 = 0

R, G, B = 12, 13, 14
for i, l in enumerate(q):
    r = list(map(int, re.findall(r"(\d+) red", l)))
    g = list(map(int, re.findall(r"(\d+) green", l)))
    b = list(map(int, re.findall(r"(\d+) blue", l)))
    
    if all([
        *([i <= R for i in r] + [i <= G for i in g] + [i <= B for i in b])
    ]):
        a1 += (i + 1)
    
print(f"Answer 1: {a1}")



#* Question 2
a2 = 0
for i, l in enumerate(q):
    r = list(map(int, re.findall(r"(\d+) red", l)))
    g = list(map(int, re.findall(r"(\d+) green", l)))
    b = list(map(int, re.findall(r"(\d+) blue", l)))
    
    a2 += max(r) * max(g) * max(b)


print(f"Answer 2: {a2}")