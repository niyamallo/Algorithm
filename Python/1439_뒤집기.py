import sys
input = sys.stdin.readline

nums = ["2"] + list(input().rstrip())
cnt_0 = 0
cnt_1 = 0
for i in range(len(nums)):
    if nums[i] == nums[i-1]:
        pass
    elif nums[i] == "0":
        cnt_0 += 1
    elif nums[i] == "1":
        cnt_1 += 1

print(min(cnt_0, cnt_1))