# https://www.hackerrank.com/challenges/input/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


# Python2

import sys
# Enter your code here. Read input from STDIN. Print output to STDOUT
# 1 4
# x**3 + x**2 + x + 1
#line = eval(raw_input(''))
#line = sys.stdin.read()
line = raw_input()
#print(line)
x, k = [float(i) for i in line.split(' ')]
poly = raw_input()
exponents = []
signs = []
zero_coefficient = 0.0
i = 0
len_poly = len(poly)
while i < len(poly) and poly[i].isspace():
    i = i + 1
if i < len_poly:
    if poly[i] == '-':
        signs.append(-1)
        i = i + 1
    elif poly[i] == '+':
        signs.append(1)
        i = i + 1
    else:
        signs.append(1)
while i < len_poly:
    if poly[i] == 'x':
        if  i + 1 < len_poly and poly[i + 1] == '*' and \
            i + 2 < len_poly and poly[i + 2] == '*':
            j = i + 3
            sign = 1
            if poly[i] == '-':
                sign = -1
                i = i + 1
            elif poly[i] == '+':
                i = i + 1
            while i < len(poly) and poly[i].isspace():
                i = i + 1
            exponent = 0
            while j < len_poly and poly[j].isdigit():
                exponent = exponent * 10 + int(poly[j])
                j = j + 1
            exponents.append(exponent * sign)
            i = j
        else:
            exponents.append(1)
            i = i + 1
    elif poly[i] == '+':
        signs.append(1)
        i = i + 1
    elif poly[i] == '-':
        signs.append(-1)
        i = i + 1
    elif poly[i].isdigit():
        n = 0.0
        j = i
        while j < len_poly and poly[j].isdigit():
            n = n * 10 + int(poly[j])
            j = j + 1
        #zero_coefficient = n
        exponents.append(0)
        i = j
    else:
        if i < len_poly and poly[i].isspace():
            while i < len(poly) and poly[i].isspace():
                i = i + 1
        else:
            i = i + 1

result = 0.0
i = 0
#print(signs.__str__())
while i < len(exponents):
    c = exponents[i]
    result = result + signs[i] * (x ** c)
    i = i + 1

result = result

print(result == k)
