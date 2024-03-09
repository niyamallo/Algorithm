import sys
input = sys.stdin.readline

n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))

if nums[2] - nums[1] == nums[1] - nums[0]:
    print(nums[-1] + nums[1] - nums[0])
else:
    print(int(nums[-1] * nums[1] / nums[0]))