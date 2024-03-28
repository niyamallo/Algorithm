import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def bfs(x, y):
    global cnt
    visited[x][y] = True
    if campus[x][y] == "P":
        cnt += 1
    for dx, dy in direction:
        if 0 <= x+dx < n and 0 <= y+dy < m:
            if campus[x+dx][y+dy] != "X" and not visited[x+dx][y+dy]:
                bfs(x+dx, y+dy)


n, m = map(int, input().split())
campus = []
for _ in range(n):
    campus.append(list(input().rstrip()))
visited = [[False]*m for _ in range(n)]

direction = [(1,0), (-1,0), (0,1), (0,-1)]
cnt = 0

for i in range(n):
    for j in range(m):
        if campus[i][j] == "I":
            bfs(i, j)
            break

if cnt:
    print(cnt)
else:
    print("TT")