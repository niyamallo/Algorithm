import sys
input = sys.stdin.readline

A = list(map(int, input().rstrip()))
B = list(map(int, input().rstrip()))

nums = []
for i in range(16):
    if i%2 == 0:
        nums.append(A[i//2])
    else:
        nums.append(B[i//2])

while len(nums) != 2:
    new_nums = []
    for i in range(len(nums)-1):
        new_nums.append((nums[i]+nums[i+1])%10)
    nums = new_nums

print(*nums, sep="")