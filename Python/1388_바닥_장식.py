import sys
input = sys.stdin.readline

def dfs(x, y):
    visited[x][y]= True
    if ground[x][y] == "-":
        if y+1 < m and ground[x][y+1] == "-" and visited[x][y+1] == False:
            dfs(x, y+1)
        else:
            return
    elif ground[x][y] == "|":
        if x+1 < n and ground[x+1][y] == "|" and visited[x+1][y] == False:
            dfs(x+1, y)
        else:
            return


n, m = map(int, input().split())
ground = []
for _ in range(n):
    ground.append(list(input().rstrip()))

visited = [[False]*m for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == False:
            dfs(i, j)
            cnt += 1

print(cnt)