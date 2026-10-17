# Problem 10: Swap Case
# HackerRank: https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    return ''.join(
        char.lower() if char.isupper()
        else char.upper() if char.islower()
        else char
        for char in s
    )

if __name__ == '__main__':
    s = input()
    print(swap_case(s))
