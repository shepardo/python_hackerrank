# https://www.hackerrank.com/challenges/no-idea/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
def dump_array(a):
    [print(x, end=' ') for x in a]
    print()

n, m = map(lambda x: int(x), input().split(' '))
a = map(lambda x: int(x), input().split(' '))
A = set(map(lambda x: int(x), input().split(' ')))
B = set(map(lambda x: int(x), input().split(' ')))
#dump_array(a)
#dump_array(A)
#dump_array(B)
happiness = 0
for x in a:
    if x in A:
        happiness += 1
    elif x in B:
        happiness -= 1
print(happiness)

