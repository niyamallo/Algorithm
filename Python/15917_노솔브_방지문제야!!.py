import sys
input = sys.stdin.readline

two = set()
for i in range(31):
    two.add(2**i)

n = int(input())
for _ in range(n):
    if int(input()) in two:
        print(1)
    else:
        print(0)