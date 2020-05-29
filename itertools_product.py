# https://www.hackerrank.com/challenges/itertools-product/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
A = map(lambda x: int(x), input().split(' '))
B = map(lambda x: int(x), input().split(' '))
[print('{0} '.format(x), end='') for x in product(A, B)]
