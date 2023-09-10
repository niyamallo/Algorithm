import sys
import itertools

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

ls = [sum(x) for x in itertools.combinations(nums, 3) if sum(x) <= m]

print(max(ls))