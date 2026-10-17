# Problem 18: The Minion Game
# HackerRank: https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    kevin_score = 0
    stuart_score = 0
    length = len(string)
    for i in range(length):
        points = length - i
        if string[i] in "AEIOU":
            kevin_score += points
        else:
            stuart_score += points
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
