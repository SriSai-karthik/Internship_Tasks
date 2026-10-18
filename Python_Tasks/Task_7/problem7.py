# Problem 7: Alphabet Rangoli
# HackerRank: https://www.hackerrank.com/challenges/py-alphabet-rangoli/problem

def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    lines = []
    for i in range(size):
        s = "-".join(alpha[size - 1:i:-1] + alpha[i:size])
        lines.append(s.center(4 * size - 3, "-"))
    print("\n".join(lines + lines[-2::-1]))

if __name__ == '__main__':
    print_rangoli(int(input()))
