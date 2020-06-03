# https://www.hackerrank.com/challenges/word-order/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
dic = {}
n = int(input())
for _ in range(n):
    word = input()
    dic.setdefault(word, 0)
    dic[word] += 1
print(len(dic))
for k in dic:
    print(dic[k], end=' ')
