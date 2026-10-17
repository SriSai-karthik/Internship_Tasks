# Problem 1: Find the Runner-Up Score!
# HackerRank: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))
    highest = max(scores)
    scores = [score for score in scores if score != highest]
    print(max(scores))
