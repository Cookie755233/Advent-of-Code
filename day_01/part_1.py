with open('./data.in') as f:
    s = 0
    l = [int(i) for i in f.readlines()]
    for i in range(len(l)-1):
        if l[i]<l[i+1]: s +=1
    
    print(s)