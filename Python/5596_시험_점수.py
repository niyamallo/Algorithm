import sys
input = sys.stdin.readline

mg = sum(list(map(int, input().split())))
ms = sum(list(map(int, input().split())))

print(max(mg, ms))