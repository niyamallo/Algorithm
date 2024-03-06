import sys
input = sys.stdin.readline

n = int(input())
ans = []

for _ in range(n):
    a, b, c = map(int, input().split())
    if a != b and b != c and c != a:
        big = max(a, b, c)
        ans.append(big * 100)
    elif a == b and b == c:
        ans.append(10000 + a * 1000)
    else:
        if a == b:
            ans.append(1000 + a * 100)
        else:
            ans.append(1000 + c * 100)

print(max(ans))