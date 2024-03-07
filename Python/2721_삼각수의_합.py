import sys
input = sys.stdin.readline

dp = [0]
tmp = 1
for i in range(2, 302):
    dp.append(dp[i-2] + (tmp+i)*(i-1))
    tmp += i

n = int(input())

for _ in range(n):
    m = int(input())
    print(dp[m])