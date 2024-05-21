n = int(input())
dp = [0]*n
if n == 1:
    print(1)
else:
    dp[0] = 1
    dp[1] = 2
    for i in range(2,n):
        dp[i] = (dp[i-1] + dp[i-2])%15746
    print(dp[-1])