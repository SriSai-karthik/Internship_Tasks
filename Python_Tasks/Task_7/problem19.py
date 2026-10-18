# Problem 19: Weighted Uniform Strings
# HackerRank: https://www.hackerrank.com/challenges/weighted-uniform-string/problem

def weightedUniformStrings(s, queries):
    weights = set()
    previous = ''
    current_weight = 0
    for char in s:
        if char == previous:
            current_weight += ord(char) - ord('a') + 1
        else:
            current_weight = ord(char) - ord('a') + 1
            previous = char
        weights.add(current_weight)
    return ["Yes" if query in weights else "No" for query in queries]

if __name__ == '__main__':
    s = input().strip()
    n = int(input().strip())
    queries = [int(input().strip()) for _ in range(n)]
    print('\n'.join(weightedUniformStrings(s, queries)))
