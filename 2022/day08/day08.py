import os
import re
import numpy as np


with open(f"{os.path.splitext(os.path.basename(__file__))[0]}.txt") as f:
    INPUT = f.read().splitlines()

# INPUT  = '''
# 30373
# 25512
# 65332
# 33549
# 35390
# '''.splitlines()[1:]


directions = ((-1, 0), (0, -1), (1, 0), (0, 1))


def explore(grid, x, y):
    visible, score = False, 1
    val = grid[y, x]
    size = grid.shape[0]
    for dy, dx in directions:
        i, curr_x, curr_y = 0, x+dx, y+dy
        while 0 <= curr_x < size and 0 <= curr_y < size:
            i += 1
            if grid[curr_y, curr_x] >= val:
                break
            curr_x += dx
            curr_y += dy
        else:
            visible = True
        score *= i
    return visible, score


def main(input: str):
    p1 = p2 = 0
    grid = []
    for l in input:
        grid.append(list(map(int, l)))
    grid = np.array(grid)

    size = grid.shape[0]
    for r in range(size):
        for c in range(size):
            visible, score = explore(grid, r, c)
            p2 = max(score, p2)
            p1 += visible

    print(f'The Answer in Part 1 is : {p1}')
    print(f'The Answer in Part 2 is : {p2}')


print(main(INPUT))
