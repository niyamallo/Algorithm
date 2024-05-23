import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        visited[x][y] = True
        dq = deque()
        dq.append((x,y))
        while dq:
            nowX, nowY = dq.popleft()
            for i in range(4):
                if 0<=nowX+dx[i]<m and 0<=nowY+dy[i]<n:
                    if not visited[nowX+dx[i]][nowY+dy[i]]:
                        visited[nowX+dx[i]][nowY+dy[i]] = True
                        dq.append((nowX+dx[i],nowY+dy[i]))

tc = int(input())
for _ in range(tc):
    
    m, n, k = map(int, input().split())
    board = [[0]*(n) for _ in range(m)]
    visited = [[True]*(n) for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        board[x][y] = 1
        visited[x][y] = False
    cnt = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)