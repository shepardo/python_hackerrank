# https://www.hackerrank.com/challenges/iterables-and-iterators/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
n = int(input())
l = input().split(' ')
r = int(input())
cnt = 0
cnt_with_a = 0
for t in combinations(l, r):
    cnt += 1
    if sum(1 if x == 'a' else 0 for x in t) > 0:
        cnt_with_a += 1
#print(cnt)
#print(cnt_with_a)
print(float(cnt_with_a) / cnt)
