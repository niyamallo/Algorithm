import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    dq = deque()
    for a in range(x):
        for b in range(y):
            if tomatos[a][b] == 1:
                dq.append((a, b))
    while dq:
        nowX, nowY = dq.popleft()
        for i in range(4):
            if 0<=nowX+dx[i]<n and 0<=nowY+dy[i]<m and tomatos[nowX+dx[i]][nowY+dy[i]] == 0:
                tomatos[nowX+dx[i]][nowY+dy[i]] = tomatos[nowX][nowY]+1
                dq.append((nowX+dx[i], nowY+dy[i]))

m, n = map(int, input().split())
tomatos = []
for _ in range(n):
    tomatos.append(list(map(int, input().split())))
dx = [1, 0, -1, 0]
dy = [0, 1, 0 ,-1]

cnt = 0
bfs(n, m)

for i in range(n):
    for j in range(m):
        if tomatos[i][j] == 0:
            print(-1)
            exit()
        else:
            cnt = max(tomatos[i][j], cnt)

print(cnt-1)