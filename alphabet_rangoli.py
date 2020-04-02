# https://www.hackerrank.com/challenges/alphabet-rangoli/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import array


'''
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----


#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

e-d-c-b-a-b-c-d-e
#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
'''

def print_rangoli(size):
    # your code goes here
    '''
    line = array.array('B', [ord('-') for _ in range(size * 4)])

    for c in range(size - 1, -1, -1):
        ch = ord('a') + c
        line[c * 2 + size * 2] = ch

    for c in range(size):
        ch = ord('a') + c
        #line[c * 2] = ch

    print("".join(map(lambda x: chr(x), line)))
    '''
    do_print(0, size)
    return

    for i in range(size):
        do_print(i, size)

def do_print(offset, size):
    i = size - 1
    while i >= offset:
        print('--', end='')
        i = i - 1

    i = size - 1
    while i >= offset:
        ch = chr(ord('a') + i)
        print('{0}-'.format(ch), end='')
        i = i - 1

    i = offset + 1
    while i < size:
        ch = chr(ord('a') + i)
        if i != size - 1:
            print('{0}-'.format(ch), end='')
        else:
            print(ch, end='')
        i = i + 1

    i = offset
    while i < size:
        print('--', end='')
        i = i + 1

    print('')


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
