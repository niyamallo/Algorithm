import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    visited[x][y] = 0
    dq = deque()
    dq.append((x, y))
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            if 0 <= x+dx < n and 0 <= y+dy < m:
                if world[x+dx][y+dy] == 1 and visited[x+dx][y+dy] == -1:
                    visited[x+dx][y+dy] = visited[x][y] + 1
                    dq.append((x+dx, y+dy))

n, m = map(int, input().split())
world = []
for _ in range(n):
    world.append(list(map(int, input().split())))
ls = []
targetX = -1
targetY = -1
for i in range(n):
    for j in range(m):
        if world[i][j] == 2:
            targetX = i
            targetY = j
        elif world[i][j] == 0:
            ls.append((i, j))

visited = [[-1]*m for _ in range(n)]
direction = [(1,0), (-1,0), (0,1), (0,-1)]
bfs(targetX, targetY)

for x, y in ls:
    visited[x][y] = 0

for nums in visited:
    print(*nums)