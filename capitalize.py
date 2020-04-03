
#!/bin/python3

# https://www.hackerrank.com/challenges/capitalize/problem?h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    arr = s.split(' ')
    arr = map(lambda x: x.capitalize(), arr)
    return ' '.join(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
