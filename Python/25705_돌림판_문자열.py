import sys; input = sys.stdin.readline

n = int(input())
ls = list(input().rstrip())
m = int(input())
strings = list(input().rstrip())
lss = ls*m

idx = 0
for i in range(m):
    if strings[i] not in ls:
        print(-1)
        exit()
    while strings[i] != lss[idx]:
        idx += 1
    idx += 1

print(idx)