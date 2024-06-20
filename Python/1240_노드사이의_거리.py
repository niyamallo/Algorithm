import sys
input = sys.stdin.readline

def dfs(start, end):
    
    visited = [False]*(n+1)
    
    st = [(start, 0)]
    visited[start] = True

    while st:
        now, total_distance = st.pop()

        if now == end:
            print(total_distance)
            break
        
        for next, distance in graph[now]:
            if not visited[next]:
                visited[next] = True
                st.append((next, total_distance + distance))

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    n1, n2, distance = map(int, input().split())
    graph[n1].append((n2, distance))
    graph[n2].append((n1, distance))

for _ in range(m):
    start, end = map(int, input().split())
    dfs(start, end)