import sys
input = sys.stdin.readline

n = int(input())

a, b, c = 1, 1, 1
for i in range(n-1):
    a, b, c = b, c, a+c

print(a)