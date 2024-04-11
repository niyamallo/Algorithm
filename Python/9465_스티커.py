import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    ls = []
    for _ in range(2):
        ls.append(list(map(int, input().split())))
    total = 0
    for i in range(1, n):
        ls[0][i] += max(total, ls[1][i-1])
        ls[1][i] += max(total, ls[0][i-1])
        total = max(ls[0][i-1], ls[1][i-1])
    print(max(ls[0][-1], ls[1][-1]))