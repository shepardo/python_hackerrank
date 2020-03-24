# https://www.hackerrank.com/challenges/python-string-formatting/problem?h_r=next-challenge&h_v=zen


#hex(64).lstrip("0x").rstrip("L")
#oct(8).lstrip("0o").rstrip("L")
#bin(10).lstrip("0b").rstrip("L")
#"ab".center(10, '*')

def print_formatted(number):
    # your code goes here
    mylen = len(bin(number).lstrip("0b").rstrip("L"))
    for i in range(number + 1):
        if i != 0:
            print(('{decimal:>%s} {octal:>%s} {hexa:>%s} {bina:>%s}'.replace('%s', str(mylen))).
                format(
                    decimal=i,
                    octal=oct(i).lstrip("0o").rstrip("L"),
                    hexa=hex(i).lstrip("0x").rstrip("L").upper(),
                    bina=bin(i).lstrip("0b").rstrip("L")))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
