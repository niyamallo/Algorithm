import sys

date = [31,28,31,30,31,30,31,31,30,31,30,31]
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

x, cnt = map(int, sys.stdin.readline().split())
for i in range(x-1):
    cnt += date[i]

remainder = cnt % 7
print(day[remainder])