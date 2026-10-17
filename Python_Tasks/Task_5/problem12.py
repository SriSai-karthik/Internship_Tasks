# Problem 12: Capitalize!
# HackerRank: https://www.hackerrank.com/challenges/capitalize/problem

def solve(s):
    result = []
    capitalize_next = True
    for char in s:
        if char.isalnum() and capitalize_next:
            result.append(char.upper())
            capitalize_next = False
        else:
            result.append(char)
        if char == ' ':
            capitalize_next = True
    return ''.join(result)

if __name__ == '__main__':
    s = input()
    print(solve(s))
