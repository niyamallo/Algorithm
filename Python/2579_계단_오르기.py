n = int(input())
ls = [int(input()) for _ in range(n)]
dp = [0]*n
dp[0] = ls[0]
if n >= 2:
    dp[1] = ls[0] + ls[1]
    for i in range(2, n):
        dp[i] = ls[i] + max(dp[i-2], dp[i-3] + ls[i-1])

print(dp[-1])