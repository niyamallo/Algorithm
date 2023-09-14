import sys

n, m = map(int, sys.stdin.readline().split())
ls = list(map(int, sys.stdin.readline().split()))

for i in range(len(ls)):
    ls[i] = m*ls[i]

ans = []

for i in range(len(ls)-1):
    ans.append(ls[i]+ls[i+1])

print(min(ans))