import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = []

def backtracking():
    if len(answer) == m:
        print(" ".join(map(str, answer)))
    else:
        for i in range(1, n+1):
            answer.append(i)
            backtracking()
            answer.pop()

backtracking()