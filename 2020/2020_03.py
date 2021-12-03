l = open('./2020_03.in').read().split('\n')


'''Part I'''
# Right 3, down 1.
col, trees = 0, 0
length = len(l[0])

for i in l:
    trees += (i[col % length] == '#')
    col+=3
        
print(trees) 



'''Part II'''
# Right 1, down 1.
# Right 3, down 1.
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

res = 1
for x, y in slopes:
    col, trees = 0, 0
    map_= l[::y]
    
    for i in map_:
        trees += (i[col % length] == '#')
        col += x
    res = res * trees

print(res) 