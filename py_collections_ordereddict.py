# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input())
dic = {}
for _ in range(n):
    line = input().strip()
    idx = line.rfind(' ')
    #print(idx)
    name, price = (line[0:idx], line[idx + 1:])
    dic.setdefault(name, 0)
    dic[name] += int(price)

for k in dic:
    print('{0} {1}'.format(k, dic[k]))
