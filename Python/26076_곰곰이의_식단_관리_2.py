import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
max_needs = n + m - 2
needs = [[max_needs] * m for _ in range(n)]

dq = deque()
for j in range(1, m):
    if board[0][j]:
        dq.appendleft((0, 0, j))
        needs[0][j] = 0
    else:
        dq.append((1, 0, j))
        needs[0][j] = 1
for i in range(1, n - 1):
    if board[i][m - 1]:
        dq.appendleft((0, i, m - 1))
        needs[i][m - 1] = 0
    else:
        dq.append((1, i, m - 1))
        needs[i][m - 1] = 1

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
while dq:
    need, i, j = dq.popleft()
    if needs[i][j] < need:
        continue
    for k in range(8):
        ni = i + dx[k]
        nj = j + dy[k]
        if 0 <= ni < n and 0 <= nj < m:
            if board[ni][nj]:
                if needs[ni][nj] > needs[i][j]:
                    needs[ni][nj] = needs[i][j]
                    dq.appendleft((needs[ni][nj], ni, nj))
            else:
                if needs[ni][nj] > needs[i][j] + 1:
                    needs[ni][nj] = needs[i][j] + 1
                    dq.append((needs[ni][nj], ni, nj))

answer = 2
for i in range(1, n):
    if needs[i][0] < answer:
        answer = needs[i][0]
for j in range(1, m - 1):
    if needs[n - 1][j] < answer:
        answer = needs[n - 1][j]

print(answer)