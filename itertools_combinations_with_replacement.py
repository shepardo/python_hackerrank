# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
s, n = input().split()
[print(''.join(item)) for item in combinations_with_replacement(sorted(s), int(n))]
