# https://www.hackerrank.com/challenges/designer-door-mat/problem?h_r=next-challenge&h_v=zen

import array

def fill_horizontal_line(line_number, m, n):
    line = array.array('B', [ord('-') for _ in range(m)])
    pos = (m // 2)
    if line_number == n // 2:
        line[pos - 3:pos + 4] = array.array('B', [ord(c) for c in [*'WELCOME']])
        return "".join(map(lambda x: chr(x), line))
    line_number = n - line_number - 1 if line_number > n // 2 else line_number
    for l in range(line_number + 1):
        pos_left = pos - l * 3
        pos_right = pos + l * 3
        line[pos_left + 1] = ord('.')
        line[pos_left] = ord('|')
        line[pos_left - 1] = ord('.')
        line[pos_right + 1] = ord('.')
        line[pos_right] = ord('|')
        line[pos_right - 1] = ord('.')
    return "".join(map(lambda x: chr(x), line))

s = input()
n, m = map( lambda x: int(x), s.split(' '))
for i in range(n):
    print(fill_horizontal_line(i, m, n))
