# Problem 5: String Validators
# HackerRank: https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()
    checks = [
        str.isalnum,
        str.isalpha,
        str.isdigit,
        str.islower,
        str.isupper
    ]
    for check in checks:
        print(any(check(c) for c in s))
