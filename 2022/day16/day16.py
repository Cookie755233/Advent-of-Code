tmp = '''\
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II'''



import os
import re
from collections import deque, Counter, defaultdict
from dataclasses import dataclass
with open(f"{os.path.splitext(os.path.basename(__file__))[0]}.txt") as f:
    INPUT = f.read().splitlines()
    
@dataclass
class Valve:
    name: str 
    flow: str
    to: list
    
    def __post_init__(self):
        self.flow = int(self.flow)
        
    def set_idx(self, idx):
        self.idx = idx
        
        
valves = []
for i, line in enumerate(tmp.splitlines()):
    name, flow, to = re.findall('Valve (.*) has flow rate=(\d+); tunnels? leads? to valves? (.*)', line)[0]
    valve = Valve(name, flow, to.split(', '))
    valve.set_idx(i)
    valves.append(valve)