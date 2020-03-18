# https://www.hackerrank.com/challenges/zipped/problem?h_r=next-challenge&h_v=zen
# Python3
line = input()
n, x = [int(i) for i in line.split(' ')]
scores = []
for i in range(x):
    line = input()
    scores.append([float(k) for k in line.split(' ')])
for i in range(n):
    score = 0.0
    for j in range(x):
        score = score + scores[j][i]
    print(score / x)
