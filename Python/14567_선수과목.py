import sys; input = sys.stdin.readline
from collections import deque

def topology_sort():
    dq = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            dq.append(i)
    
    for i in range(1, n+1):
        now = dq.popleft()

        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                dq.append(next)
            answer[next] = answer[now] + 1

n, m = map(int, input().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

answer = [1] * (n+1)
topology_sort()

print(*answer[1:])