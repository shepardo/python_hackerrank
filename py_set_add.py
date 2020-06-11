# https://www.hackerrank.com/challenges/py-set-add/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
s = set()
n = int(input())
for _ in range(n):
    line = input()
    s.add(line)
print(len(s))
