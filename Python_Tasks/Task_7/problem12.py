# Problem 12: Making Anagrams
# HackerRank: https://www.hackerrank.com/challenges/making-anagrams/problem

from collections import Counter

def makingAnagrams(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    return sum((c1 - c2).values()) + sum((c2 - c1).values())

if __name__ == '__main__':
    print(makingAnagrams(input().strip(), input().strip()))
