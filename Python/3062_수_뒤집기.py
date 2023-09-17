import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    a = sys.stdin.readline().rstrip()
    b = int(a)+int(a[::-1])
    if str(b) == str(b)[::-1]:
        print("YES")
    else:
        print("NO")