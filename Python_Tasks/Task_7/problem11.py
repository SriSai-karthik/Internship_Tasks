# Problem 11: Two Strings
# HackerRank: https://www.hackerrank.com/challenges/two-strings/problem

def twoStrings(s1, s2):
    return "YES" if set(s1) & set(s2) else "NO"

if __name__ == '__main__':
    p = int(input().strip())
    for _ in range(p):
        s1 = input().strip()
        s2 = input().strip()
        print(twoStrings(s1, s2))
