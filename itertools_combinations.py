# https://www.hackerrank.com/challenges/itertools-combinations/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s, n = input().split()

for i in range(int(n)):
    [print(''.join(item)) for item in combinations(sorted(s), i + 1)]
