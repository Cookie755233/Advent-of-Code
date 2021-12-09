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


f = open('./data_04.in').read().split('\n\n')

calls = [int(i) for i in f[0].split(',')]
boards = f[1:]

def bingo_when(calls):
    board = [[0 for _ in range(5)]for _ in range(5)]
    for call in calls:
        i, j = call//5, call%5
        board[i][j] = 1
        for r in range(5):
            if board[r]==[1]*5 or all([board[c][r]==1 for c in range(5)]): 
                return call


first, winner = 10000, None
last, last_winner = 0, None
for i, board in enumerate(boards): 
    nums_in_board = [int(i) for i in board.split()]
    marked_nums = [num for num in calls if num in nums_in_board]
    called_indexes = [nums_in_board.index(m) for m in marked_nums]
    bingo_number = bingo_when(called_indexes)
    when_win = calls.index(nums_in_board[bingo_number])

    if first > when_win:
        first = when_win
        winner = i
    if last < when_win:
        last = when_win
        last_winner = i

'''Part I'''
print(first, winner)
print(sum([0 if i in calls[0:first+1] 
            else i for i in [int(j) for j in boards[winner].split()]]) * calls[first])

'''Part II'''
print(last, last_winner)
print(sum([0 if i in calls[0:last+1] 
            else i for i in [int(j) for j in boards[last_winner].split()]]) * calls[last])

