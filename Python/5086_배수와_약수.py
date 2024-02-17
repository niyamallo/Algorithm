import sys
input = sys.stdin.readline

for _ in range(10001):
    a, b = map(int, input().split())
    if a == 0:
        break
    if b%a == 0:
        print("factor")
    elif a%b == 0:
        print("multiple")
    else:
        print("neither")