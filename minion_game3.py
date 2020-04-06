def minion_game(string):
    vowels = frozenset("AIEOU")
    lens = len(string)

    kevin = sum( i for i, c in enumerate(reversed(string)) if c in vowels) + lens
    stuart = ( lens * (lens + 1) ) // 2 - kevin

    if stuart > kevin:
        print(f"Stuart {stuart}")
    elif kevin > stuart:
        print(f"Kevin {kevin}")
    else:
        print("Draw")
