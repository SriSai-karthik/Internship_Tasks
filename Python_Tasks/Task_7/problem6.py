# Problem 6: Pangrams
# HackerRank: https://www.hackerrank.com/challenges/pangrams/problem

def pangrams(s):
    letters = set(s.lower())
    return "pangram" if set('abcdefghijklmnopqrstuvwxyz').issubset(letters) else "not pangram"

if __name__ == '__main__':
    print(pangrams(input()))
