import sys
input = sys.stdin.readline

lst = set()
res = 0
for _ in range(5):
    a = int(input())
    if a in lst:
        res -= a
        lst.discard(a)
    else:
        lst.add(a)
        res += a
print(res)