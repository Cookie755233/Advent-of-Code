with open('./data.in') as f:
    s = 0
    l = [int(i) for i in f.readlines()]
    for i in range(len(l)-3):
        if sum(l[i:i+3])<sum(l[i+1:i+4]): s +=1
    
    print(s)