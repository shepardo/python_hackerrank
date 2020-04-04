# https://www.hackerrank.com/challenges/the-minion-game/problem?h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_r=next-challenge&h_v=zen

vowels = 'AEIOU'

kevsc = 0
stusc = 0
def minion_game(s):
    global kevsc
    global stusc
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print("Kevin {0}".format(kevsc))
    elif kevsc < stusc:
        print("Stuart {0}".format(stusc))
    else:
        print("Draw")



if __name__ == '__main__':
    s = input()
    minion_game(s)
