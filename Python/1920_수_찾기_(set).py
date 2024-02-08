import sys
input = sys.stdin.readline

n = int(input())
ns = set(input().split())
m = int(input())
ms = input().split()

for m in ms:
    if m in ns:
        print(1)
    else:
        print(0)