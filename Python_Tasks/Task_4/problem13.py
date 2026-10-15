# Problem 13: Symmetric Difference
# HackerRank: https://www.hackerrank.com/challenges/symmetric-difference/problem

m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))

for value in sorted(a.symmetric_difference(b)):
    print(value)
