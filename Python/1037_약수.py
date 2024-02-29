import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

if len(nums) == 1:
    print(nums[0]**2)
else:
    nums.sort()
    print(nums[0]*nums[-1])