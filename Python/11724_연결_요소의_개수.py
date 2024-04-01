import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    visited[start] = True
    dq = deque()
    dq.append(start)
    while dq:
        now = dq.popleft()
        for i in ls[now]:
            if not visited[i]:
                visited[i] = True
                dq.append(i)

n, m = map(int, input().split())
ls = [[]for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    ls[a].append(b)
    ls[b].append(a)
visited = [False]*(n+1)
visited[0] = True
cnt = 0

for i in range(1, n+1):
    if not visited[i]:
        if not ls[i]:
            cnt += 1
            visited[i] = True
        else:
            cnt += 1
            bfs(i)

print(cnt)