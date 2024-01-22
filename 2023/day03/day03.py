
import os


# with open(os.path.join(os.path.dirname(__file__), f"{os.path.splitext(__file__)[0]}.test")) as f:
with open(os.path.join(os.path.dirname(__file__), f"{os.path.splitext(__file__)[0]}.in")) as f:
    grid = f.read().split("\n")


coords_of_first_part_number = set()

for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char.isdigit() or char == '.':
            continue
        
        for current_row in [r - 1, r, r + 1]:
            for current_col in [c - 1, 1, c + 1]:
                if current_row < 0 or current_row >= len(grid) or\
                    current_col < 0 or current_col >= len(grid[current_row]) or\
                        not grid[current_row][current_col].isdigit():
                    continue
                    
                while current_col > 0 and grid[current_row][current_col-1].isdigit():
                    current_col -= 1
                    
                coords_of_first_part_number.add((current_row, current_col))

list_of_nums = []
for r, c in coords_of_first_part_number:
    literal_num = ""
    while c < len(grid[r]) and grid[r][c].isdigit():
        literal_num += grid[r][c]
        c += 1
        
    list_of_nums.append(int(literal_num))
    
print(f"Answer 1: {sum(list_of_nums)}")




total = 0
for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char != '*':
            continue
        
        coords_of_first_gear = set()
        
        for current_row in [r - 1, r, r + 1]:
            for current_col in [c - 1, c, c + 1]:
                if current_row < 0 or current_row >= len(grid) or\
                    current_col < 0 or current_col >= len(grid[current_row]) or\
                        not grid[current_row][current_col].isdigit():
                    continue
                while current_col > 0 and grid[current_row][current_col - 1].isdigit():
                    current_col -= 1
                coords_of_first_gear.add((current_row, current_col))
                

        if len(coords_of_first_gear) != 2:
            continue
        
        list_of_nums = []
        
        for cr, cc in coords_of_first_gear:
            literal_num = ""
            while cc < len(grid[cr]) and grid[cr][cc].isdigit():
                literal_num += grid[cr][cc]
                cc += 1
            list_of_nums.append(int(literal_num))

        total += list_of_nums[0] * list_of_nums[1]   
        
print(f"Answer 1: {total}")