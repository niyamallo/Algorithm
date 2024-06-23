import sys; input = sys.stdin.readline
from math import inf

def find_shortest_node():

    shortest = inf
    index = 0

    for i in range(1, n+1):
        if distance[i] < shortest and not visited[i]:
            shortest = distance[i]
            index = i

    return index

def dijkstra(start):
    
    distance[start] = 0
    visited[start] = True

    for n2, d in graph[start]:
        distance[n2] = d

    for _ in range(n-1):
        now = find_shortest_node()
        visited[now] = True

        for n2, d in graph[now]:
            if distance[now] + d < distance[n2]:
                distance[n2] = distance[now] + d

    return

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    n1, n2, d = map(int, input().split())
    graph[n1].append((n2, d))
    graph[n2].append((n1, d))
visited = [False] * (n+1)
distance = [inf] * (n+1)
s, t = map(int, input().split())


dijkstra(s)
print(distance[t])