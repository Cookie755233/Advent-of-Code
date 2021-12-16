
from collections import defaultdict

# [0] for test data, [1] for big data
f = open('./2020_14.in').read().split('\n\n')[1].splitlines()

groups,temp = [], []
while f:
    x = f.pop()
    if x.startswith('mask'):
        temp.append(x)
        groups.append(temp)
        temp = []
    else:
        temp.append(x)

D = defaultdict(int)
for i in groups[:2]:
    mask = i.pop().split()[-1]

    for mem in i[::-1]:
        m = mem.split()[0][4:-1]
        v = mem.split()[-1]
        idx = bin(int(v))[2:].rjust(36, '0')
        idx = ''.join(
            [idx[x] if mask[x]=='X' else mask[x] for x in range(36)])

        D[m] = int(idx, 2)

print(sum(D.values())) # HWWHYHYWHWYYWYYYY???

# def indices(newidx, floating):
#     if len(floating) == 0:
#         return [newidx]
#     else:
#         b0 = floating[0]
#         rest = floating[1:]
#         ans = indices(newidx,rest) + indices(newidx+2**b0, rest)
#         return ans

# def modify_value(value, mask):
#     newvalue = 0
#     for i,bit in enumerate(reversed(mask)):
#         if bit == 'X':
#             newvalue += (value & (2**i))
#         elif bit == '1':
#             newvalue += 2**i
#         elif bit == '0':
#             pass
#         else:
#             assert False
#     return newvalue

# def modify_idx(idx, mask):
#     newidx = 0
#     floating = []
#     for i,bit in enumerate(reversed(mask)):
#         ibit = idx & (2**i)
#         if bit == 'X':
#             floating.append(i)
#         elif bit == '1':
#             newidx += 2**i
#         elif bit == '0':
#             newidx += ibit
#             pass
#         else:
#             assert False
#     return indices(newidx, floating)

# def solve(p1):
#     mask = ''
#     mem = {}
#     lines = list(f)
#     for line in lines:
#         line = line.strip()
#         if line.startswith('mask'):
#             newmask = line.split()[-1]
#             mask = newmask
#         else:
#             assert len(mask) == 36
#             idx,_,value = line.split()
#             idx = int(idx.split('[')[-1][:-1])
#             value = int(value)
#             I = [idx]
#             if p1:
#                 value = modify_value(value, mask)
#             else:
#                 I = modify_idx(idx, mask)

#             for idx2 in I:
#                 mem[idx2] = value

#     ans = 0
#     for k,v in mem.items():
#         ans += v
#     return ans

# print(solve(True))
# print(solve(False))