import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dq = deque()
    dq.append((x, y, 0))
    visited[x][y][0] = 1
    while dq:
        a, b, c = dq.popleft()
        if a == n - 1 and b == m - 1:
            return visited[a][b][c]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if miro[nx][ny] == 1 and c == 0:
                    visited[nx][ny][1] = visited[a][b][0] + 1
                    dq.append((nx, ny, 1))
                elif miro[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    visited[nx][ny][c] = visited[a][b][c] + 1
                    dq.append((nx, ny, c))
    return -1

n, m = map(int, input().split())
miro = []
for _ in range(n):
    miro.append(list(map(int, input().rstrip())))
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

print(bfs(0, 0))