# https://www.hackerrank.com/challenges/merge-the-tools/problem?h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# AAB CAA ADA

def merge_the_tools(string, k):
    # your code goes here
    d = {}
    for i in range(len(string)):
        c = string[i]
        if i % k == 0 and i != 0:
            print('')
            d = {}
            d[c] = 1
            print(c, end='')
        elif d.get(c) == None:
            print(c, end='')
            d[c] = 1
    print('')


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
