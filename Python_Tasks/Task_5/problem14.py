# Problem 14: Finding the Percentage
# HackerRank: https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *marks = input().split()
        student_marks[name] = list(map(float, marks))

    query_name = input()
    scores = student_marks[query_name]
    average = sum(scores) / len(scores)
    print(f"{average:.2f}")
