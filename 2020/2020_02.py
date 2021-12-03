
passwords = open('./2020_02.in').readlines()

'''Part I'''
valid = 0
for password in passwords:
    num, ch, p = password.split()
    min_, max_ = num.split('-')

    if int(min_) <= p.count(ch[0]) <= int(max_):
        valid += 1
        
print(valid)



'''Part II'''
valid = 0
for password in passwords:
    pos, ch, p = password.split()
    i, j = pos.split('-')
    if (p[int(i)-1] == ch[0] and p[int(j)-1] != ch[0]) or\
        (p[int(i)-1] != ch[0] and p[int(j)-1] == ch[0]):
        valid += 1
    
print(valid)