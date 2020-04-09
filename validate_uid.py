# https://www.hackerrank.com/challenges/validating-uid/problem?h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
A valid UID must follow the rules below:

It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits (0-9).
It should only contain alphanumeric characters (a-z, A-Z, 0-9)
No character should repeat.
There must be exactly 10 characters in a valid UID.
'''
def validate(s):
    digits = 0
    upper_letters = 0
    chars = {}
    if len(s) != 10:
        return False
    for c in s:
        if c.isdigit():
            digits += 1
        elif c.isupper():
            upper_letters += 1
        if not c.isalnum():
            return False
        if chars.get(c) != None:
            return False
        else:
            chars[c] = 1
    if digits < 3:
        return False
    if upper_letters < 2:
        return False
    return True

n = int(input())
for i in range(n):
    s = input()
    if validate(s):
        print('Valid')
    else:
        print('Invalid')
