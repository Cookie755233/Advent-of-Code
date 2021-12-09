
f = open('./2020_09.in').read().split('\n')
l = [int(i) for i in f]
start = 25

# Part I
ans_1 = None
for num in l[start:]:
    if not ans_1:
        prev = l[start-25:start]
        check = []
        for i, n in enumerate(prev):
            if i+1 <len(prev):
                for j in prev[i+1:]:
                    check.append([n, j])
    
        for s in check:
            if sum(s) == num:
                start += 1
                break
        else: ans_1 = num
        
print(ans_1) # 2089807806


# Part II
ans_2_lst = None
check = 2
index = l.index(ans_1)

while not ans_2_lst:
    for i, e in enumerate(l[:index-check]):
        checklst = [l[i+j] for j in range(check)]
       
        if sum(checklst) == ans_1:
            ans_2_lst = checklst
        
    check+=1


ans_2_lst.sort()
ans_2 = ans_2_lst[0] + ans_2_lst[-1]
print(ans_2) # 245848639

        