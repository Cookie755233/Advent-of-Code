f = open('./data_21.in').read().splitlines()
p1, p2 = f[0].split()[-1], f[1].split()[-1]
#8, 2

score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 1  # how many 3 times it's rolled, answer*3-1
c1, c2 = 0, 0  # count(scores)
p1, p2 = 7, 1  # position
start = 1  # starting point of each round

while c1 < 1000 and c2 < 1000:
    if i % 2 == 1:
        p1 += 3*start + 3
        c1 += score[p1 % 10]
        i += 1
        start += 3

    else:
        p2 += 3*start + 3
        c2 += score[p2 % 10]
        i += 1
        start += 3

ans_1 = min(c1, c2) * ((i-1)*3)
print(ans_1)

# part 2
p1 = 8-1
p2 = 2-1
DP = {} # game state -> answer for that game state
def count_win(p1, p2, s1, s2):
  # Given that A is at position p1 with score s1, and B is at position p2 with score s2, and A is to move,
  # return (# of universes where player A wins, # of universes where player B wins)
  if s1 >= 21:
    return (1,0)
  if s2 >= 21:
    return (0, 1)
  if (p1, p2, s1, s2) in DP:
    return DP[(p1, p2, s1, s2)]
  ans = (0,0)
  for d1 in [1,2,3]:
    for d2 in [1,2,3]:
      for d3 in [1,2,3]:
        new_p1 = (p1+d1+d2+d3)%10
        new_s1 = s1 + new_p1 + 1

        x1, y1 = count_win(p2, new_p1, s2, new_s1)
        ans = (ans[0]+y1, ans[1]+x1)
  DP[(p1, p2, s1, s2)] = ans
  return ans

print(max(count_win(p1, p2, 0, 0)))