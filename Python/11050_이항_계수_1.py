import sys

n, k = map(int, sys.stdin.readline().split())

def factorial(n):
    if n ==0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

ans = int(factorial(n)/(factorial(n-k)*factorial(k)))

print(ans)