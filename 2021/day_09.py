
from functools import reduce

f = open('./data_09.in').read().split('\n')
l = [[int(j)for j in str(i)] for i in f]

low_points = basins =  []

def basin_size(n, i, j, seen):
    dirs = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]

    for r, c in dirs:
        if 0<=r<len(l) and 0<=c<len(l[0]):
            if n < l[r][c] < 9:
                seen.add((r, c))
                basin_size(l[r][c], r, c, seen)
                
    return len(seen)+1  # include itself


    
for i in range(len(l)):
    for j in range(len(l[0])):
        dirs = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        
        # Part 1
        if all( [l[i][j] < l[r][c] for r,c in dirs if 0<=r<len(l) and 0<=c<len(l[0])] ):
            low_points.append(l[i][j])
            
            # Part 2
            seen = set()
            basin = basin_size(l[i][j], i, j, seen)
            basins.append(basin)

basins.sort(reverse=True)

ans1 = sum([int(i)+1 for i in low_points])
ans2 = reduce(lambda x, y: x*y, basins[0:3])
    
print(f'Answer 1: {ans1}') 
print(f'Answer 2: {ans2}')