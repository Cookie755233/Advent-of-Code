
'''
Every chunk must open and close with one of four legal pairs of matching characters: ()/ <>/ {}/ []
Stop at the first incorrect closing character on each corrupted line.

take the first illegal character on the line and look it up in the following table:

): 3 points.
]: 57 points.
}: 1197 points.
>: 25137 points.

What is the total syntax error score for those errors?
'''


from collections import Counter

f = open('./data_10.in').read().splitlines()
lst = [[str(i) for i in x] for x in f]

open_brackets = ['{', '[', '(', '<']
close_brackets = ['}', ']', ')', '>']
scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

invalid = []
for line in lst:
    seen = []
    for i, syn in enumerate(line):
        if syn in open_brackets:
            seen.append(syn)
        
        else:
            if seen[-1] == open_brackets[close_brackets.index(syn)]:
                seen.pop(-1)
            else:
                invalid.append(syn)
                break
            

d = Counter(invalid)
ans_1 = sum([scores[k]*d[k] for k in d.keys()])
print(ans_1)
    
                
'''
Now, discard the corrupted lines. The remaining lines are incomplete.

Incomplete lines don't have any incorrect characters - instead, they're missing some closing characters at the end of the line. To repair the navigation subsystem, you just need to figure out the sequence of closing characters that complete all open chunks in the line.

You can only use closing characters ), ], }, or >

The score is determined by considering the completion string character-by-character. Start with a total score of 0. Then, for each character, multiply the total score by 5 and then increase the total score by the point value given for the character in the following table:

): 1 point.
]: 2 points.
}: 3 points.
>: 4 points.

the winner is found by sorting all of the scores and then taking the middle score. What is the middle score?
'''


open_brackets = ['{', '[', '(', '<']
close_brackets = ['}', ']', ')', '>']
scores_2 = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}

completion_scores = []
for line in lst:
    remain = []
    for i, syn in enumerate(line):
        
        if syn in open_brackets:
            remain.append(syn)
        
        else:
            if remain[-1] == open_brackets[close_brackets.index(syn)]:
                remain.pop(-1)

    # print(remain)
    score=0
    for r in remain[::-1]:
        score = score*5 + scores_2[r]
    completion_scores.append(score)

completion_scores.sort()
print(completion_scores)
ans_2 = completion_scores[len(completion_scores)//2]        
print(ans_2)





pairs = ["()", "[]", "<>", "{}"]
bad_scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
good_scores = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}


def parse(line):
    stack = []
    for char in line:
        good = False
        for p in pairs:
            if char == p[0]:
                stack.append(char)
                good = True
            elif char == p[1]:
                if stack[-1] == p[0]:
                    stack.pop()
                    good = True

        if not good:
            return bad_scores[char]

    return 0


def complete(line):
    stack = []
    ans = 0
    for char in line:
        for p in pairs:
            if char == p[0]:
                stack.append(char)
            elif char == p[1]:
                if stack[-1] == p[0]:
                    stack.pop()

    for c in stack[::-1]:
        ans *= 5
        ans += good_scores[c]

    return ans


# Delete corrupted stuff
data = [line for line in f if parse(line) == 0]

scores = []
for line in data:
    scores.append(complete(line))

scores.sort()
print(scores)
ans = scores[len(scores) // 2]
print(ans)











