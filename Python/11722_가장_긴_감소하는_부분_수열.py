import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [0]*n

for i in range(n):
    for j in range(i):
        if nums[i] < nums[j] and dp[j] > dp[i]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))