import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c = int(input())

hour = a + c//60
min = b + c%60

if min >= 60:
    min -= 60
    hour += 1
if hour >= 24:
    hour -= 24

print(hour, min)