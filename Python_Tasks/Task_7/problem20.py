# Problem 20: Super Reduced String
# HackerRank: https://www.hackerrank.com/challenges/reduced-string/problem

def superReducedString(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack) if stack else "Empty String"

if __name__ == '__main__':
    print(superReducedString(input().strip()))
