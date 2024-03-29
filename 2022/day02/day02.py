import os

with open(f'{os.path.splitext(os.path.basename(__file__))[0]}.txt') as f:
    INPUT = f.read()


part_one = {"A X": 4, "A Y": 8, "A Z": 3,
            "B X": 1, "B Y": 5, "B Z": 9,
            "C X": 7, "C Y": 2, "C Z": 6}
part_two = {"A X": 3, "A Y": 4, "A Z": 8,
            "B X": 1, "B Y": 5, "B Z": 9,
            "C X": 2, "C Y": 6, "C Z": 7}

p1 = sum(part_one[i] for i in INPUT.splitlines())
p2 = sum(part_two[i] for i in INPUT.splitlines())

print(f'The Answer in Part 1 is : {p1}')
print(f'The Answer in Part 2 is : {p2}')
