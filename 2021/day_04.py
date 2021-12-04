'''
all numbers in any row or any column of a board are marked,
that board wins. (Diagonals don't count.)

The score of the winning board can now be calculated. 
Start by finding the sum of all unmarked numbers on that board; 
in this case, the sum is 188. 
Then, multiply that sum by the number that was just called when the board won, 24, 
to get the final score, 188 * 24 = 4512.

What will your final score be if you choose that board?
'''

f = open('./data_04.txt').read().split('\n\n')

calls = [int(i) for i in f[0].split(',')]

boards = f[1:]

def bingo_when(calls):
    board = [[0 for _ in range(5)]for _ in range(5)]
    for n, call in enumerate(calls):
        i, j = call//5, call%5
        board[i][j] = 1
        for r in range(5):
            if board[r]==[1]*5: return n
            if all([board[c][r]==1 for c in range(5)]): return n


first, winner = 10000, None

for i, board in enumerate(boards): 
    num_lst = [int(i) for i in board.split()]
    marked = [num for num in calls if num in num_lst]
    index = [num_lst.index(m) for m in marked]
    win_order = bingo_when(index)
    if first > win_order:
        first = win_order
        winner = i

print([n for n in [int(i) for i in boards[winner].split()[first:]]])
print(calls[first] * sum([n for n in [int(i) for i in boards[winner].split()[first:]]]))