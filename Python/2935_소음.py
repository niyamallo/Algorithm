import sys
input = sys.stdin.readline

num1 = int(input())
cal = input().rstrip()
num2 = int(input())

if cal == "*":
    ans = num1 * num2
else:
    ans = num1 + num2

print(ans)