import sys
input = sys.stdin.readline

ls = []
tmp = 0
for _ in range(4):
    a, b = map(int, input().split())
    tmp = tmp - a + b
    ls.append(tmp)

print(max(ls))