s, k = map(int, input().split())

nums = [0]*k
tmp = 0
while tmp < s:
    nums[tmp%k] += 1
    tmp += 1

ans = 1
for num in nums:
    ans *= num

print(ans)