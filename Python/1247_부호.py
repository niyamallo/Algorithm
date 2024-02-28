import sys
input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    total = 0
    for _ in range(n):
        total += int(input())
    if total == 0:
        print(0)
    elif total > 0:
        print("+")
    else:
        print("-")