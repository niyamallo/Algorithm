import sys
input = sys.stdin.readline

n = int(input())
scores = [0] + list(map(int, input().split()))
point = 0
total = 0
for i in range(n+1):
    if scores[i] == 0:
        point = 0
    else:
        point += 1
        total += point

print(total)