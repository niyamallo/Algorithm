import sys

n, m = map(int, sys.stdin.readline().split())
nums = [x for x in range(1, n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    change = nums[a-1:b][::-1]
    nums[a-1:b] = change

print(*nums)
