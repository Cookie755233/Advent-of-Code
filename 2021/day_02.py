f = open ('./data_02.in')
moves = f.readlines()


''' Part I '''
v, h = 0, 0
horizontal, depth = 0, 0
for move in moves:
    instr, X = move.split()
    X = int(X)
    match instr:
        case 'forward': horizontal += X
        case 'down': depth += X
        case 'up': depth -= X
print(horizontal * depth)



''' Part II'''
horizontal, depth, aim = 0, 0, 0
for move in moves:
    instr, X = move.split()
    X = int(X)
    match instr:
        case 'forward': horizontal += X; depth = depth + (aim * X)
        case 'down': aim += X
        case 'up': aim -= X
print(horizontal * depth)


        
