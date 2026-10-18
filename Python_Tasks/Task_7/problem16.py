# Problem 16: Caesar Cipher
# HackerRank: https://www.hackerrank.com/challenges/caesar-cipher-1/problem

def caesarCipher(s, k):
    result = []
    k %= 26
    for char in s:
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + k) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + k) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    int(input().strip())
    s = input().strip()
    k = int(input().strip())
    print(caesarCipher(s, k))
