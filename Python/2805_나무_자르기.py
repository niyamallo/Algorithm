import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort(reverse=True)
total = 0
high = trees[0]
short = 0

while short <= high:
    mid = (high + short) // 2
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid
        else:
            break
    if total >= m:
        short = mid + 1
    else:
        high = mid - 1

print(high)