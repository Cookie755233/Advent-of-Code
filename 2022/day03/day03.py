import os

with open(f"{os.path.splitext(os.path.basename(__file__))[0]}.txt") as f:
    INPUT = f.read().splitlines()
letters = "abcdefghijklmnopqrstuvwxyz"
POINTS = {v: i + 1 for i, v in enumerate(letters + letters.upper())}

p1 = 0
for line in INPUT:
    l = int(len(line) / 2)
    a, b = line[:l], line[l:]
    corr = [i for i in a if i in b][0]
    p1 += POINTS[corr]

p2 = 0
elfs = []
for i, line in enumerate(INPUT):
    if (i + 1) % 3 == 0:
        elfs.append(line)
        a, b, c = elfs
        corr = [i for i in a if (i in b and i in c)][0]
        p2 += POINTS[corr]
        elfs.clear()
    else:
        elfs.append(line)


print(f"The Answer in Part 1 is : {p1}")
print(f"The Answer in Part 2 is : {p2}")
