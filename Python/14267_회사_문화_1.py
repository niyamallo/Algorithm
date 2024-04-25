import sys
input = sys.stdin.readline

def dfs(a):
    stack = [a]

    while stack:
        now = stack.pop()
        for i in tree[now]:
            dp[i] += dp[now]
        stack += tree[now]
        
n, m = map(int, input().split())
ls = list(map(int, input().split()))
tree = [[] for x in range(n+1)]
for i in range(1, len(ls)):
    tree[ls[i]].append(i+1)
dp = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    dp[a] += b

dfs(1)

print(*dp[1:])