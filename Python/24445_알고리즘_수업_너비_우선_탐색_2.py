import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    dq = deque()
    visited[x] = 1
    dq.append(x)
    cnt = 1

    while dq:
        now = dq.popleft()
        for i in sorted(graph[now], reverse=True):
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                dq.append(i)

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1)

bfs(r)

print(*visited[1:], sep="\n")