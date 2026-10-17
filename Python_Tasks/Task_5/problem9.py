# Problem 9: Word Order
# HackerRank: https://www.hackerrank.com/challenges/word-order/problem

if __name__ == '__main__':
    n = int(input())
    word_counts = {}
    for _ in range(n):
        word = input()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    print(len(word_counts))
    print(*word_counts.values())
