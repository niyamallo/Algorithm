import sys
input = sys.stdin.readline

n = int(input())
ls = []

for _ in range(n):
    ls.append(list(map(int, input().split())))

for i in range(1, n):
    ls[i][0] += ls[i-1][0]
    for j in range(1,i):
        ls[i][j] += max(ls[i-1][j-1], ls[i-1][j])
    ls[i][-1] += ls[i-1][-1]

print(max(ls[-1]))