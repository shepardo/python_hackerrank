# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
d = defaultdict(list)
m, n = [int(x) for x in input().split(' ')]
for i in range(m):
    d[input()].append(i + 1)

for i in range(n):
    l = d[input()]
    if len(l) > 0:
        [print(x, end=' ') for x in l]
        print('')
    else:
        print(-1)
