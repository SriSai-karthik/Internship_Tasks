# Problem 17: Separate the Numbers
# HackerRank: https://www.hackerrank.com/challenges/separate-the-numbers/problem

def separateNumbers(s):
    for i in range(1, len(s) // 2 + 1):
        first = s[:i]
        number = int(first)
        current = first
        while len(current) < len(s):
            number += 1
            current += str(number)
        if current == s:
            print("YES", first)
            return
    print("NO")

if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        separateNumbers(input().strip())
