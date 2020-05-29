# https://www.hackerrank.com/challenges/itertools-permutations/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s, n = input().split(' ')
l = list(permutations(list(s), int(n)))
l.sort()
[print(''.join(x)) for x in l]

