import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
ls.sort()
now = 0
total = 0

for i in range(n):
    now = now + ls[i]
    total += now

print(total)