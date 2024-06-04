import sys
import math
input = sys.stdin.readline

def find_distance(x, y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

def find_parents(x):
    if parents[x] != x:
        parents[x] = find_parents(parents[x])
    return parents[x]

def union(x, y):
    x = parents[x]
    y = parents[y]
    if x != y:
        parents[x] = y

n = int(input())
stars = []
distance = []
parents = [x for x in range(n)]
for _ in range(n):
    a, b = map(float, input().split())
    stars.append((a, b))
for i in range(n):
    for j in range(i+1, n):
        distance.append((i, j, find_distance(stars[i], stars[j])))
distance.sort(key=lambda x:x[2])

total_distance = 0
for a, b, c in distance:
    if find_parents(a) != find_parents(b):
        union(a, b)
        total_distance += c

print(round(total_distance, 2))