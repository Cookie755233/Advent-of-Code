
f = open('./data_05.in').read().split('\n')

sky = [[0 for _ in range(1000)] for _ in range(1000)]
for line in f:
    r = line.split('->')
    x1, y1, x2, y2 = [int(i) for i in (r[0].split(',') + r[1].split(',')) ]
    dx, dy = x2-x1, y2-y1
    a, b, c, d = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)
    
    # part I
    if x1 == x2:
        for i in range(c, d+1):
            sky[x1][i] += 1
    elif y1 == y2:
        for i in range(a, b+1):
            sky[i][y1] += 1
    # part II
    else:
        r = [i for i in range(x1, x2+1, 1)] if x1<x2 else [i for i in range(x1, x2-1, -1)]
        c = [i for i in range(y1, y2+1, 1)] if y1<y2 else [i for i in range(y1, y2-1, -1)]
        for i, j in zip(r, c):
            sky[i][j] += 1

res = 0
for r in sky:
    for c in r:
        if c>1:res+=1

print(res)