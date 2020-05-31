# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
import re

def split(txt):
    return [s for s in re.split("[,|;\W]+", txt)]

def split2(txt, seps):
    default_sep = seps[0]
    # we skip seps[0] because that's the default separator
    for sep in seps[1:]:
        txt = txt.replace(sep, default_sep)
    return [i.strip() for i in txt.split(default_sep)]

n = int(input())
Student = namedtuple('Student', input())
sum_marks = 0
for _ in range(n):
    data = split(input())
    #[print(x) for x in data]
    student = Student(data[0], data[1], data[2], data[3])
    sum_marks += int(student.MARKS)

print(float(sum_marks) / n)
