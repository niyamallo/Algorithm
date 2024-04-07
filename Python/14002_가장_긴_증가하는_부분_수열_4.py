import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [0]*n
big = 0
answer = []
answer_dict = {0:[]}


for i in range(n):
    tmp = -1
    for j in range(i):
        if nums[i] > nums[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
            tmp = j
    dp[i] += 1
    if dp[i] > dp[big]:
        big = i
    if tmp == -1:
        answer_dict[i] = [nums[i]]
    else:
        answer_dict[i] = answer_dict[tmp] + [nums[i]]

print(dp[big])
print(*answer_dict[big])