
from collections import Counter

f = open('./2020_10.in').read().split('\n')
l = sorted([int(i) for i in f])

# Part 1
diff = []
for i in range(len(l)-1):
    if i == 0:
        diff.append(l[i])
    diff.append(l[i+1]-l[i])
    
    if i+2 == len(l):
        diff.append(3)

d = Counter(diff)
# print(d)
print( d.get(1) * d.get(3) )


# Part 2

adapters = [0] + l
valid_arrangements = [1] * len(adapters)
for index in range(1, len(adapters)):
    valid_arrangements[index] = sum(
        valid_arrangements[src_index]
        for src_index in range(max(0, index - 3), index)
        if adapters[index] - adapters[src_index] <= 3
    )



print(valid_arrangements[-1])