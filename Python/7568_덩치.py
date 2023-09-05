import sys

n = int(input())
ls = []
ans = []

for i in range(n):
    ls.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    cnt = 0
    for j in range(n):
        if ls[i][0] < ls[j][0] and ls[i][1] < ls[j][1]:
            cnt += 1
    ans.append(cnt+1)
print(*ans)