import sys

ls = list(map(ord, sys.stdin.readline().rstrip()))

ans = [0]*26
for i in ls:
    ans[i-97] += 1

print(*ans)