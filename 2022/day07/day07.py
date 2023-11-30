
import os
import re
from collections import deque, Counter, defaultdict


with open(f"{os.path.splitext(os.path.basename(__file__))[0]}.txt") as f:
    INPUT = f.read().splitlines()

p1, p2 = 0, 0
tmp ='''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
'''

class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.children = []
        self.parent = None
        self.val = 0

    def add_parent(self, parent):
        self.parent=parent
        
    def add_child(self, obj):
        self.children.append(obj)
        
    def add_val(self, val):
        self.val += val


def compute(node: Node, limit=100_000):
    if node.name == '/': return 0
    
    val = node.val 
    if node.children:
        for child in node.children:
            child_val = compute(child) 
            val += child_val
    print(node.name, val)
    return val
    if val < limit:
        return val
    else:
        return 0

    
def compute_nodes(node:Node):
    tot = 0
    if node.children:
        tot += compute(node)
        for child in node.children:
            tot += compute(child)
    return tot

D = {}

tot = 0
curr = None
# for i, cli in enumerate(tmp.splitlines()[:7]):
for i, cli in enumerate(INPUT):
    if cli.startswith('$ cd'):
        if cli == '$ cd ..':
            curr = curr.parent
        else:
            child = Node(cli.split()[-1])
            if not curr:
                curr = child
            else:
                curr.add_child(child)
                child.add_parent(curr)
            
    elif cli.startswith('$ ls'): 
        curr = child
    
    elif cli.startswith('dir'):
        pass
    #     child = Node(cli.split()[-1])
    #     child.add_parent(curr)
        # curr.add_child(child)
    
    else:
        size, file = cli.split()
        curr.add_val(int(size))


while curr.parent:
    curr = curr.parent
print(D)
print('ans: ' + str(compute_nodes(curr)))

print(f'The Answer in Part 1 is : {p1}')
print(f'The Answer in Part 2 is : {p2}')
                