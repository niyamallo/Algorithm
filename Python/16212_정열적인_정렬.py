import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
ls.sort()
print(*ls)