import sys
input = sys.stdin.readline

k, n = map(int, input().split())
ls = []
for _ in range(k):
    ls.append(int(input()))

start = 1
end = max(ls)
while start <= end:
    mid = (start+end)//2
    lan = 0
    for i in ls:
        lan += i//mid
    if lan >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)