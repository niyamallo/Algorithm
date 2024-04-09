import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp_up = [0]*n
dp_down = [0]*n

for i in range(n):
    for j in range(i):
        if nums[j] < nums[i] and dp_up[j] > dp_up[i]:
            dp_up[i] = dp_up[j]
    dp_up[i] += 1

for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if nums[j] < nums[i] and dp_down[j] > dp_down[i]:
            dp_down[i] = dp_down[j]
    dp_down[i] += 1

total = -1
for i in range(n):
    if dp_up[i] + dp_down[i] > total:
        total = dp_up[i] + dp_down[i]

print(total-1)