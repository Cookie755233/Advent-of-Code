import re
f = open('./2020_04.in').read().split('\n\n')

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID) Not neccessary
'''Part I'''
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

valid = 0
valid_infos = []
for person in f:
    info = person.split()
    info_str = ''.join(info)
    if all([i in info_str for i in fields]):
        valid += 1
        valid_infos.append(info)
print(valid)


'''Part II'''  
# Rules:
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

f = open('./2020_04.in').read()
keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
passwords = f.split('\n\n')
s1 = s2 = 0 # for Q1, Q2
for password in passwords:
    fields = re.split('[\n ]', password)
    d = dict(field.split(':') for field in fields)
    if all(key in d for key in keys):
        s1 += 1
        if 1920 <= int(d['byr']) <= 2002\
                and 2010 <= int(d['iyr']) <= 2020\
                and 2020 <= int(d['eyr']) <= 2030\
                and re.match(r'\d+..', d['hgt'])\
                and (d['hgt'].endswith('cm') and 150 <= int(d['hgt'][:-2]) <= 193 or d['hgt'].endswith('in') and 59 <= int(d['hgt'][:-2]) <= 76)\
                and re.match(r'^#[\da-f]{6}$', d['hcl'])\
                and d['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']\
                and re.match(r'^\d{9}$', d['pid']):
            s2 += 1
print(s1, s2)
