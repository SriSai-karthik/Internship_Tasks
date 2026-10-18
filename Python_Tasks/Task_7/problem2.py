# Problem 2: The Captain's Room
# HackerRank: https://www.hackerrank.com/challenges/py-the-captains-room/problem

if __name__ == '__main__':
    k = int(input())
    rooms = list(map(int, input().split()))
    unique_rooms = set(rooms)
    print((sum(unique_rooms) * k - sum(rooms)) // (k - 1))
