'''
Start by considering the whole range, rows 0 through 127. (128 rows)
The first 7 characters will either be F or B
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44.

The last three characters will be either L or R; 
these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7).
Start by considering the whole range, columns 0 through 7.
R means to take the upper half, keeping columns 4 through 7.
L means to take the lower half, keeping columns 4 through 5.
The final R keeps the upper of the two, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column. 
In this example, the seat has ID 44 * 8 + 5 = 357.

What is the highest seat ID on a boarding pass?
'''


l = open('./2020_05.in').read().split('\n')
'''Part I'''

res = 0

def get_row(string):
    s, e = 0, 127
    for i in string:
        if i =='F': e = (e+s)//2
        else: s = (e+s)/2+1
    return s
def get_col(string):
    s, e = 0, 7
    for i in string:
        if i == 'R': s = (e+s)/2+1
        else: e = (e+s)//2
    return e

for p in l:
    row = get_row(p[0:7])
    col = get_col(p[7:])
    res = max(row*8 + col, res)
    
print(res)

''' Part II '''


        
            
# Binary Solution
'''part I'''
seats = [int(x.replace('F','0').replace('B','1').replace('L','0').replace('R','1'), 2) for x in l]
seats.sort()
print(seats[-1])


'''part II'''
for x in range(len(seats)):
    if seats[x+1] - seats[x] != 1:
        print(seats[x] + 1)
        break