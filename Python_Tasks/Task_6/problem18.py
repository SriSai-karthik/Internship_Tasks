# Problem 18: Set Mutations
# HackerRank: https://www.hackerrank.com/challenges/py-set-mutations/problem

n = int(input())
a = set(map(int, input().split()))
operations = int(input())

for _ in range(operations):
    command, size = input().split()
    other_set = set(map(int, input().split()))

    if command == "intersection_update":
        a.intersection_update(other_set)
    elif command == "update":
        a.update(other_set)
    elif command == "symmetric_difference_update":
        a.symmetric_difference_update(other_set)
    elif command == "difference_update":
        a.difference_update(other_set)

print(sum(a))
