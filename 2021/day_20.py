
import pprint as pp

f = open('./data_20.in').read().splitlines()


alg, img = f[0], f[2:]
R, C = len(img), len(img[0])


def img_enhance(r, c, n):  
    dx = [-1, -1 ,-1, 0 ,0 ,0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    bistr = ''
    for x, y in zip(dx, dy):
        if 0<=r+x<R and 0<=c+y<C:
            if img[r+x][c+y] == '#': bistr += '1'
            if img[r+x][c+y] == '.': bistr += '0'
        else:
            # starts with 1 ( range(1,x) ), so invert the options
            if   n % 2 == 1: bistr += '0'
            elif n % 2 == 0: bistr += '1'
            
    return alg[int(bistr, 2)]

for i in range(1,51): # runs twice
    # row, col expands by 1 in each side after each enhancement
    after = [['-' for _ in range(R+2)] for _ in range(C+2)]
    
    for r in range(R+2):
        for c in range(C+2):
            # after's (0, 0) is before's(-1, -1)
            after[r][c] = img_enhance(r-1, c-1, i) 
    
    img = after
    R, C = R+2, C+2


print( sum([l.count('#') for l in img]) ) 

#!/usr/bin/python3

# rule, start = open('./data_20.in').read().split('\n\n')
# rule = rule.strip()
# assert len(rule) == 512

# G = set()
# for r,line in enumerate(start.strip().split('\n')):
#   for c,x in enumerate(line.strip()):
#     if x=='#':
#       G.add((r,c))

# # on=true means G says what pixels are on (all the rest are off).
# # on=false means G says what pixels are *off* (all the rest are on)
# def step(G, on):
#   G2 = set()
#   min_r = min([r for r,c in G])
#   max_r = max([r for r,c in G])
#   min_c = min([c for r,c in G])
#   max_c = max([c for r,c in G])
#   for r in range(min_r-5, max_r+10):
#     for c in range(min_c-5, max_c+10):
#       rc_str = 0
#       bit = 8
#       for dr in [-1, 0, 1]:
#         for dc in [-1, 0, 1]:
#           if ((r+dr,c+dc) in G) == on:
#             rc_str += 2**bit
#           bit -= 1
#       assert 0<=rc_str < 512
#       if (rule[rc_str] == '#') != on:
#         G2.add((r,c))
#   return G2

# def show(G):
#   min_r = min([r for r,c in G])
#   max_r = max([r for r,c in G])
#   min_c = min([c for r,c in G])
#   max_c = max([c for r,c in G])
#   for r in range(min_r-5, max_r+5):
#     row = ''
#     for c in range(min_c-5, max_c+5):
#       if (r,c) in G:
#         row += '#'
#       else:
#         row += ' '
#     print(row)
  
# for t in range(50):
#   # show(G)
#   if t==2:
#     print(len(G))
#   G = step(G, t%2==0)
# print(len(G))

