
import os

problems = [
    ("Set .symmetric_difference() Operation", "https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem", '''n = int(input())
english = set(map(int, input().split()))
m = int(input())
french = set(map(int, input().split()))
print(len(english.symmetric_difference(french)))'''),

    ("The Captain's Room", "https://www.hackerrank.com/challenges/py-the-captains-room/problem", '''if __name__ == '__main__':
    k = int(input())
    rooms = list(map(int, input().split()))
    unique_rooms = set(rooms)
    print((sum(unique_rooms) * k - sum(rooms)) // (k - 1))'''),

    ("Mars Exploration", "https://www.hackerrank.com/challenges/mars-exploration/problem", '''def marsExploration(s):
    expected = "SOS" * (len(s) // 3)
    return sum(1 for a, b in zip(s, expected) if a != b)

if __name__ == '__main__':
    s = input().strip()
    print(marsExploration(s))'''),

    ("Funny String", "https://www.hackerrank.com/challenges/funny-string/problem", '''def funnyString(s):
    r = s[::-1]
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(r[i]) - ord(r[i - 1])):
            return "Not Funny"
    return "Funny"

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        print(funnyString(input().strip()))'''),

    ("Alternating Characters", "https://www.hackerrank.com/challenges/alternating-characters/problem", '''def alternatingCharacters(s):
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            deletions += 1
    return deletions

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        print(alternatingCharacters(input().strip()))'''),

    ("Pangrams", "https://www.hackerrank.com/challenges/pangrams/problem", '''def pangrams(s):
    letters = set(s.lower())
    return "pangram" if set('abcdefghijklmnopqrstuvwxyz').issubset(letters) else "not pangram"

if __name__ == '__main__':
    print(pangrams(input()))'''),

    ("Alphabet Rangoli", "https://www.hackerrank.com/challenges/py-alphabet-rangoli/problem", '''def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    lines = []
    for i in range(size):
        s = "-".join(alpha[size - 1:i:-1] + alpha[i:size])
        lines.append(s.center(4 * size - 3, "-"))
    print("\\n".join(lines + lines[-2::-1]))

if __name__ == '__main__':
    print_rangoli(int(input()))'''),

    ("Gemstones", "https://www.hackerrank.com/challenges/gem-stones/problem", '''def gemstones(arr):
    common = set(arr[0])
    for rock in arr[1:]:
        common.intersection_update(rock)
    return len(common)

if __name__ == '__main__':
    n = int(input().strip())
    arr = [input().strip() for _ in range(n)]
    print(gemstones(arr))'''),

    ("Beautiful Binary String", "https://www.hackerrank.com/challenges/beautiful-binary-string/problem", '''def beautifulBinaryString(b):
    return b.count("010")

if __name__ == '__main__':
    n = int(input().strip())
    b = input().strip()
    print(beautifulBinaryString(b))'''),

    ("CamelCase", "https://www.hackerrank.com/challenges/camelcase/problem", '''def camelcase(s):
    return 1 + sum(1 for char in s if char.isupper())

if __name__ == '__main__':
    print(camelcase(input().strip()))'''),

    ("Two Strings", "https://www.hackerrank.com/challenges/two-strings/problem", '''def twoStrings(s1, s2):
    return "YES" if set(s1) & set(s2) else "NO"

if __name__ == '__main__':
    p = int(input().strip())
    for _ in range(p):
        s1 = input().strip()
        s2 = input().strip()
        print(twoStrings(s1, s2))'''),

    ("Making Anagrams", "https://www.hackerrank.com/challenges/making-anagrams/problem", '''from collections import Counter

def makingAnagrams(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    return sum((c1 - c2).values()) + sum((c2 - c1).values())

if __name__ == '__main__':
    print(makingAnagrams(input().strip(), input().strip()))'''),

    ("Sherlock and the Valid String", "https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem", '''from collections import Counter

def isValid(s):
    counts = Counter(Counter(s).values())
    if len(counts) == 1:
        return "YES"
    if len(counts) != 2:
        return "NO"
    (f1, c1), (f2, c2) = sorted(counts.items())
    if f1 == 1 and c1 == 1:
        return "YES"
    if f2 == f1 + 1 and c2 == 1:
        return "YES"
    return "NO"

if __name__ == '__main__':
    print(isValid(input().strip()))'''),

    ("Anagram", "https://www.hackerrank.com/challenges/anagram/problem", '''from collections import Counter

def anagram(s):
    if len(s) % 2 != 0:
        return -1
    mid = len(s) // 2
    return sum((Counter(s[:mid]) - Counter(s[mid:])).values())

if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        print(anagram(input().strip()))'''),

    ("Game of Thrones - I", "https://www.hackerrank.com/challenges/game-of-thrones/problem", '''from collections import Counter

def gameOfThrones(s):
    odd_counts = sum(1 for count in Counter(s).values() if count % 2 != 0)
    return "YES" if odd_counts <= 1 else "NO"

if __name__ == '__main__':
    print(gameOfThrones(input().strip()))'''),

    ("Caesar Cipher", "https://www.hackerrank.com/challenges/caesar-cipher-1/problem", '''def caesarCipher(s, k):
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
    print(caesarCipher(s, k))'''),

    ("Separate the Numbers", "https://www.hackerrank.com/challenges/separate-the-numbers/problem", '''def separateNumbers(s):
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
        separateNumbers(input().strip())'''),

    ("String Construction", "https://www.hackerrank.com/challenges/string-construction/problem", '''def stringConstruction(s):
    return len(set(s))

if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        print(stringConstruction(input().strip()))'''),

    ("Weighted Uniform Strings", "https://www.hackerrank.com/challenges/weighted-uniform-string/problem", '''def weightedUniformStrings(s, queries):
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
    print('\\n'.join(weightedUniformStrings(s, queries)))'''),

    ("Super Reduced String", "https://www.hackerrank.com/challenges/reduced-string/problem", '''def superReducedString(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack) if stack else "Empty String"

if __name__ == '__main__':
    print(superReducedString(input().strip()))''')
]

folder = os.path.dirname(os.path.abspath(__file__))

readme = "# Python Tasks - Task 7\n\nHackerRank solutions in the assigned question order.\n\n"

for i, (name, url, code) in enumerate(problems, start=1):
    filename = f"problem{i}.py"
    with open(os.path.join(folder, filename), "w", encoding="utf-8") as f:
        f.write(f"# Problem {i}: {name}\n# HackerRank: {url}\n\n{code}\n")
    readme += f"{i}. [{name}]({url}) - `{filename}`\n"

with open(os.path.join(folder, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme)

print("Task 7 created successfully: 20 Python files and README.md.")
