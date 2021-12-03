f = open('./data_03.in').read().split('\n')


''' Part I '''
s = []
for i in range(len(f[0])):
    col = []
    for j in range(len(f)):
        col.append(f[j][i])
    s.append(col.count('1')>len(f)/2)
    
bx = ['1' if i else '0' for i in s]
by = ['0' if i else '1' for i in s]
ix = int(''.join(bx), 2)
iy = int(''.join(by), 2)
print(ix * iy)


''' Part II '''
'''
To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, 
and keep only numbers with that bit in that position. 
If 0 and 1 are equally common, keep values with a 1 in the position being considered.

To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, 
and keep only numbers with that bit in that position. If 0 and 1 are equally common, 
keep values with a 0 in the position being considered.
'''

def check_ones(lst, n, reverse=False):
    one, zero = 0, 0 
    for i in lst:
        if int(i[n]): one += 1
        else: zero += 1
        
    if not reverse: return one>=zero
    else:
        return one>zero

for i in range(len(f[0])):
    pass