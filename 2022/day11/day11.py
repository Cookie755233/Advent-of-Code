
import os
import re
from collections import deque, Counter, defaultdict


with open(f"{os.path.splitext(os.path.basename(__file__))[0]}.txt") as f:
    INPUT = f.read()
    
TMP ='''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1'''

notes = TMP.title().split('\n\n')

def operation_func(operation: str, Old):
    operate = ''.join( re.findall('Operation: New = (.*)', operation)[0] )
    operate = '(' + operate + ') // 3'
    def func(Old):
        return eval(operate)
    
    return func
            

def test_func(test: str, item: int | str):
    div = re.findall('(\d+)', test)[0]
    return int(item) % int(div) == 0
    

class Monkey:
    def __init__(self, name, item_str, operation_str, test_str, T, F) -> None:
        self.name = re.findall('(Monkey \d+)', name)[0]
        self.item_list = [int(i) for i in re.findall('Starting Items: (.*)', item_str)[0].split(',')]
        self.operation_str = operation_str
        self.test_str = test_str
        self.T = T
        self.F = F
        self.mk_business = 0
        
    def operate(self, item):
        func = operation_func(self.operation_str, item)
        # print(f'before: {item} -> after: {func(item)}')
        return func(item)

    def test(self, item_operated):
        return test_func(self.test_str, item_operated)
    
    def behave(self, item, item_operated ,divisible: bool):
        self.item_list.remove(item)
        if divisible:
            true_target = re.findall('(Monkey \d+)', self.T)[0]
            MONKEYS[true_target].item_list.append(item_operated)
        else:            
            false_target = re.findall('(Monkey \d+)', self.F)[0]
            MONKEYS[false_target].item_list.append(item_operated)
            

MONKEYS = {}
for part in notes:
    name, items, operation, test, T, F = [i.strip() for i in part.splitlines()]
    monkey = Monkey(name, items, operation, test, T, F)
    MONKEYS[monkey.name] = monkey
    
for _ in range(1000):
    for name, monkey in MONKEYS.items():
        items = monkey.item_list.copy()
        mk_business = len(items)
        monkey.mk_business += mk_business
        for item in items:
            # print(f'curently on {name}, item:{item}')
            # print([(k, v.item_list) for k,v in MONKEYS.items()])
            item_operated = monkey.operate(item)
            divisible = monkey.test(item_operated)
            monkey.behave(item, item_operated, divisible)
            # print([(k, v.item_list) for k,v in MONKEYS.items()])

print(sorted([monkey.mk_business for _,monkey in MONKEYS.items()]))
