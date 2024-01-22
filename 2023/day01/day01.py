
import re
import os

with open(
    os.path.join(
        os.path.dirname(__file__),
        f"{os.path.splitext(__file__)[0]}.in"
        )
    )as f:
    q = f.readlines()

#* Question 1
a1= 0
for l in q:
    tenth, digit = None, None
    for i in l:
        if i.isdigit():
            tenth = int(i)
            break
    for i in l[::-1]:
        if i.isdigit():
            digit = int(i)
            break
    a1 += ( 10*tenth + digit )
    
print(f"Answer 1: {a1}")

#* Question 2 
digitnames = ['one','two','three','four','five','six','seven','eight','nine']
def translate(v: str) -> str:
    return v if v.isdigit() else str(digitnames.index(v)+1)

a2 = 0
for l in q:
    nums = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', l)
    a2 += int(translate(nums[0]) + translate(nums[-1]))
    
print(f"Answer 2: {a2}")
