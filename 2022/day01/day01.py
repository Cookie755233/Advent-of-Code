with open('day01.txt') as f:
    data = f.read().splitlines()    
    
elf = dict()
tmp, elf_cnt = 0, 0
for d in data:
    try:
        tmp += int(d)
    except ValueError:
        elf[str(elf_cnt)] = tmp
        tmp = 0
        elf_cnt += 1
        continue

# Solution 1
sorted_elf = sorted(elf.items(), key=lambda item: item[1])
print(
    sorted_elf[-1]
)
# Solution 2
print(
    sum([i[-1] for i in sorted_elf[-3:]])
)
