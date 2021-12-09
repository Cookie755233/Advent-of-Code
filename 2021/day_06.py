
from collections import defaultdict, Counter

f = open('./data_06.in').read().split(',')
l = [int(x) for x in f]

d = Counter(l)

def solve(dict_, n):
    X = dict_
    for _ in range(n):
        Y = defaultdict(int)
        for x,cnt in X.items():
            if x==0:
                Y[6] += cnt
                Y[8] += cnt
            else:
                Y[x-1] += cnt
        X = Y
    return sum(X.values())

print(solve(d, 80))
print(solve(d, 256))