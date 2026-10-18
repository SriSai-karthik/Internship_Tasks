# Problem 14: Anagram
# HackerRank: https://www.hackerrank.com/challenges/anagram/problem

from collections import Counter

def anagram(s):
    if len(s) % 2 != 0:
        return -1
    mid = len(s) // 2
    return sum((Counter(s[:mid]) - Counter(s[mid:])).values())

if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        print(anagram(input().strip()))
