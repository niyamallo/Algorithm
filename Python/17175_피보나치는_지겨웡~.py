import sys
input = sys.stdin.readline

n = int(input())
a, b = 1, 1

for i in range(n):
    a, b = (a+b+1)%1000000007, a%1000000007

print(b)