import os

with open(f"{os.path.splitext(os.path.basename(__file__))[0]}.txt") as f:
    INPUT = f.read().splitlines()

p1, p2 = 0, 0

for line in INPUT:

    a,b = line.split(',')
    fa, ba = int(a.split('-')[0]), int(a.split('-')[1])
    fb, bb = int(b.split('-')[0]), int(b.split('-')[1])
    if (fa<=fb and ba>=bb) or (fb<=fa and bb>=ba):
        p1 += 1
    if (fa <= fb <= ba) or (fb <= fa <= bb):
        p2 +=1
        

print(f"The Answer in Part 1 is : {p1}")
print(f"The Answer in Part 2 is : {p2}")