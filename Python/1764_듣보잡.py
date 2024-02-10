import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ans = []
not_hear = set()

for n in range(n):
    not_hear.add(input().rstrip())

for m in range(m):
    not_see = input().rstrip()
    if not_see in not_hear:
        ans.append(not_see)

ans.sort()
print(len(ans))
print(*ans, sep="\n")