import sys
input = sys.stdin.readline

n = int(input())
ls = []
for _ in range(n):
    ls.append(list(map(int, input().split())))

ls.sort(key=lambda x : (x[-1], x[0]))

for i in range(n):
    print(*ls[i])