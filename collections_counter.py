# https://www.hackerrank.com/challenges/collections-counter/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())
#a = []
line = input()
#map(lambda x: a.append(int(x)), [x for x in line.split(' ')])
counters = Counter([int(x) for x in line.split(' ')])
profit = 0
n = int(input())
for i in range(n):
    data = input().split(' ')
    price = int(data[1])
    shoe_size = int(data[0])
    cnt = counters[shoe_size]
    if not (cnt is None) and cnt > 0:
        counters[shoe_size] = cnt - 1
        profit += price
print(profit)
