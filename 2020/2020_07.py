import re
from collections import defaultdict

f = open('./2020_07.in').read().split('\n')
bags = defaultdict(dict)

for l in f:
    parent = re.match(r'(.*) bags contain', l).groups()[0]
    for n, color in re.findall(r'(\d+) (\w+ \w+) bag', l):
        bags[parent][color] = int(n)
        
def part1():
    answer = set()
    def search(color):
        for b in bags:
            if color in bags[b]:
                answer.add(b)
                search(b)
    search('shiny gold')
    return len(answer)

def part2():
    def search(bag):
        count = 1
        for s in bags[bag]:
            multiplier = bags[bag][s]
            count += multiplier * search(s)
        return count
    return search('shiny gold' ) - 1  # Remove one for shiny gold itself

print(part1(), part2())