# https://www.hackerrank.com/challenges/find-a-string/problem
def count_substring(string, sub_string):
    n = 0
    idx = -1
    while idx < len(string):
        idx = string.find(sub_string, idx + 1) 
        if idx != -1:
            n += 1
        else:
            idx = len(string)
    return n

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
