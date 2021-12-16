'''
Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
'''

from collections import defaultdict, Counter

f = open('./data_14.in').read().splitlines()
S, rules = f[0], f[2:]

R = defaultdict(dict)
for rule in rules:
    left, right = rule.split(' -> ')
    R[left] = right

# part 1
# for _ in range(10):
#     T = ''
#     for i in range(len(S)):
#         T += S[i]
#         if i+1 < len(S):
#             T += R[S[i] + S[i+1]]
#     S = T
    
    
# C = Counter(S)
# print(max(C.values())-min(C.values()))



# Merged part I & II
C1 = Counter()
for i in range(len(S)-1):
    C1[S[i]+S[i+1]] += 1

for t in range(41):
    if t in [10,40]:
        # CF = {character: how many times that character appears}
        CF = Counter()
        # Most letters are both the first letter *and* the second letter of a pair.
        # If we take the first letter of each pair, we count every character except the last one.
        # But the last character is the same as the last character of the original string!
        # We never add characters to the end.
        # So just add that.
        for k in C1:
            CF[k[0]] += C1[k]
        CF[S[-1]] += 1
        print(max(CF.values())-min(CF.values()))

    # If AB->R, then AB becomes (AR, RB)
    C2 = Counter()
    for k in C1:
        C2[k[0]+R[k]] += C1[k]
        C2[R[k]+k[1]] += C1[k]
    C1 = C2
