# https://www.hackerrank.com/challenges/py-collections-deque/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
n = int(input())
for _ in range(n):
    line = input()
    if line.startswith('appendleft'):
        d.appendleft(line.split(' ')[1])        
    elif line.startswith('append'):
        d.append(line.split(' ')[1])
    elif line == 'pop':
        d.pop()
    elif line == 'popleft':
        d.popleft();
    #[print(x, end=' ') for x in d]
    #print('')

[print(x, end=' ') for x in d]
