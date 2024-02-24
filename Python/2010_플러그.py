import sys
input = sys.stdin.readline

n = int(input())
ans = 0
for i in range(n):
    ans += int(input())

print(ans-n+1)
