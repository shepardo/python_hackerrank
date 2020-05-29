# https://www.hackerrank.com/challenges/itertools-permutations/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s, n = input().split(' ')
l = list(permutations(list(s), int(n)))
l.sort()
[print('{0}{1}'.format(x[0], x[1])) for x in l]
