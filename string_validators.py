
# https://www.hackerrank.com/challenges/string-validators/problem



if __name__ == '__main__':
    s = input()

    has_alnum = False
    has_alpha = False
    has_digit = False
    has_uppercase = False
    has_lowercase = False

    for c in s:
        if c.isalnum():
            has_alnum = True
        if c.isalpha():
            has_alpha = True
        if c.isdigit():
            has_digit = True
        if c.isupper():
            has_uppercase = True
        if c.islower():
            has_lowercase = True

    print(has_alnum)
    print(has_alpha)
    print(has_digit)
    print(has_lowercase)
    print(has_uppercase)
