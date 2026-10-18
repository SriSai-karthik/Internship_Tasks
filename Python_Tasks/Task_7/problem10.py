# Problem 10: CamelCase
# HackerRank: https://www.hackerrank.com/challenges/camelcase/problem

def camelcase(s):
    return 1 + sum(1 for char in s if char.isupper())

if __name__ == '__main__':
    print(camelcase(input().strip()))
