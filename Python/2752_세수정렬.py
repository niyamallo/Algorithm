import sys

nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

print(*nums)