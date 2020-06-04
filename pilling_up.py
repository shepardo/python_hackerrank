# https://www.hackerrank.com/challenges/piling-up/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
def can_be_pilled_up(d):
    prev = 2**31
    while len(d) != 0:
        if d[0] >= d[-1]:
            item = d.popleft()
        else:
            item = d.pop()
        if prev < item:
            return False
        prev = item

    return True


n = int(input())
for _ in range(n):
    na = int(input())
    a = deque()
    [a.append(x) for x in map(lambda x: int(x), input().split(' '))]
    #[print(x, end=' ') for x in a]
    print('Yes' if can_be_pilled_up(a) else 'No')

