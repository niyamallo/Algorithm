import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    direction = [(1,0), (0,1), (-1,0), (0,-1)]
    dq = deque()
    dq.append((x, y))

    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            if 0 <= x+dx < n and 0 <= y+dy < m:
                if miro[x+dx][y+dy] == 1 and not visited[x+dx][y+dy]:
                    dq.append((x+dx, y+dy))
                    visited[x+dx][y+dy] = visited[x][y] + 1
    print(visited[n-1][m-1])
    
n, m = map(int, input().split())
miro = []
for _ in range(n):
    miro.append(list(map(int, input().rstrip())))
visited = [[0]*m for _ in range(n)]
visited[0][0] = 1

bfs(0, 0)