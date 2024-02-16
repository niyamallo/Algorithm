import sys
import datetime
input = sys.stdin.readline

first = list(map(int, input().split()))
second = list(map(int, input().split()))

if second[0] - first[0] > 1000:
    print("gg")
elif second[0] - first[0] == 1000 and (first[1], first[2]) <= (second[1], second[2]):
    print("gg")
else:
    print(f'D-{(datetime.date(second[0], second[1], second[2]) - datetime.date(first[0], first[1], first[2])).days}')