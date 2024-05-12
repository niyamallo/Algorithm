import sys
input = sys.stdin.readline

n, m = map(int, input().split())
for _ in range(n):
    a = input().rstrip()
    print(a[::-1])