
from time import perf_counter

''' PART I'''
with open('./2020_01.in') as f:
    t1 = perf_counter()
    l =[int(i) for i in f.readlines() if 0<int(i)<2020]
    l.sort()
    reverse = list(reversed(l))
    
    i = 0
    out = None
    while i < len(l):
        remainder = 2020-l[i]
        for b in reverse:
            if remainder < b: 
                index = reverse.index(b)
                reverse = reverse[index:] # This shorten the list by a lot
            elif remainder == b:
                out = l[i]*b 
                break
        i += 1
    t2 = perf_counter()
print(out, (t2-t1))


''' PART II'''
with open('./day_1.in') as f:
    t1 = perf_counter()
    nums =[int(i) for i in f.readlines() if 0<int(i)<2020]
    nums.sort()
    # Solution 1 (fast)
    res = False
    for i in range(len(nums) - 2):
        if i == 0 or (i > 0 and nums[i] != nums[i-1]) and not res:
            j, k, target = i + 1, len(nums) - 1, 2020 - nums[i]
            while j < k:
                if nums[j] + nums[k] < target: j += 1
                elif nums[j] + nums[k] > target: k -=1
                elif nums[j] + nums[k] == target:
                    res = nums[i] * nums[j] * nums[k]
                    break
    t2 = perf_counter()
    
    print(res, t2-t1)
        
    
    # Solution 2 (slow)
    out = False
    for x in l:
        for y in l[1:]:
            for z in l[2:]:
                if x+y+z == 2020:
                    out = x*y*z
                    t2 = perf_counter()
                    print(out, t2-t1)
                    break
            if out: break
        if out: break
        


