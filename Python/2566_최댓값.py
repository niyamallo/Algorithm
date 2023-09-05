import sys

graph = []
big = -1
x = 0
y = 0

for _ in range(9):
    graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j] > big:
            big = graph[i][j]
            x = i+1
            y = j+1

print(big)
print(x, y)