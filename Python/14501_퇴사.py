import sys
input = sys.stdin.readline

n = int(input())
ls = []
for i in range(n):
    ls.append(list(map(int, input().split())))

dp = [0]*(n+1)

for i in range(n):
    for j in range(i+ls[i][0], n+1):
        if dp[j] < dp[i] + ls[i][1]:
            dp[j] = dp[i] + ls[i][1]
print(dp[-1])
