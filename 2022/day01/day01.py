import os

with open(f'{os.path.splitext(os.path.basename(__file__))[0]}.txt') as f:
    INPUT = f.read()

    
def compute(data: str, 
            part: bool) -> int:
    # part 1
    if not part:
        p1 = max(
                sum(int(line) for line in elf.splitlines())
                for elf in data.split('\n\n')
            )
        
        print(f'The Answer in Part 1 is : {p1}')
    
    # part 2
    else:
        elfs = sorted(
            sum(int(line) for line in elf.splitlines())
            for elf in data.split('\n\n')
        )
        
        p2 = sum(elfs[-3:])
        
        print(f'The Answer in Part 2 is : {p2}')
        
if __name__ == '__main__':
    compute(INPUT, 0)
    compute(INPUT, 1) 
        