import sys
import math
input = sys.stdin.readline

n, a, b = map(int, input().split())

big = max(a, b)
small = min(a, b)
cnt = 0

while small < big:
    small = math.ceil(small/2)
    big = math.ceil(big/2)
    cnt += 1

print(cnt)