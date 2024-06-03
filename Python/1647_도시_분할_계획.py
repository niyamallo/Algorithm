import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

N, M = map(int, input().split())
parent = [x for x in range(N+1)]
roads = []
for _ in range(M):
    a, b, c = map(int, input().split())
    roads.append((a, b, c))
roads.sort(key = lambda x:x[2])

total = 0
high_value = 0
for a, b, c in roads:
    if find_parent(a) != find_parent(b):
        union(a, b)
        total += c
        high_value = c

print(total-high_value)