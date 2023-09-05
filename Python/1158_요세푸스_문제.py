import sys

n, k = map(int, sys.stdin.readline().split())
ls = [ x for x in range(1, n+1)]
idx = 0
ans = []

for i in range(n):
    idx += k-1
    if idx >= len(ls):
        idx = idx%len(ls)
    ans.append(str(ls.pop(idx)))

print("<" + ", ".join(ans) + ">")