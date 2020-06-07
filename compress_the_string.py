# https://www.hackerrank.com/challenges/compress-the-string/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
line = input()
for k, g in groupby(list(line)):
    print('({1}, {0}) '.format(k, sum(1 for _ in g)), end='')

    
