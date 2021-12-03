f = open('./data_01.in')
l = [int(i) for i in f.readlines()]

''' Part I '''
s = 0
for i in range(len(l)-1):
    if l[i]<l[i+1]: s +=1

print(s)

''' Part II'''
s = 0
for i in range(len(l)-3):
    if sum(l[i:i+3])<sum(l[i+1:i+4]): s +=1

print(s)