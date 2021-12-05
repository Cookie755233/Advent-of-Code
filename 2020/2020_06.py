f = open('./2020_06.in').read().split('\n\n')

ans_1 = ans_2 = 0
for group in f:
    l1 = []
    for i in [list(set(i)) for i in group.split()]:
        for n in i:
            if n not in l1:
                l1.append(n) 
    ans_1 += len(l1)
    
    l2 = []
    for i in l1:
        if all([i in li for li in group.split()]):
            l2.append(i)
    
    ans_2 += len(l2)
    
    
print(ans_1, ans_2)
