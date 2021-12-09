
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
print(d)
print( d.get(1) * d.get(3) )


# Part 2
ans_2 = 1
l = [0] + l

for i in range(1,len(l)):
    cnt = sum([l[i]-j in l for j in range(1,4)])
    print(cnt)
    ans_2 *= cnt
print(ans_2)