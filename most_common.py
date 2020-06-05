# https://www.hackerrank.com/challenges/most-commons/problem
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict

def cmp_items(a, b):
    if a[1] > b[1]:
        return 1
    elif a[1] < b[1]:
        return -1
    else:
        if a[0] > b[0]:
            return 1
        elif a[0] < b[0]:
            return -1
        else:
            return 0

if __name__ == '__main__':
    s = sorted(input())
    d = OrderedDict({})  #, key=lambda x: x[0])
    for c in s:
        d.setdefault(c, 0)
        d[c] += 1    
    l = []
    for k in d:
        l.append((k, d[k]))
    #sorted(l, cmp=cmp_items)
    #[print(x) for x in l]
    l = sorted(l, key=lambda x: (-x[1], x[0]))
    #[print(x) for x in l]
    for i in range(3):
        print('{0} {1}'.format(l[i][0], l[i][1]))
