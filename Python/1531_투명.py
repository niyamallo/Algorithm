import sys
input = sys.stdin.readline

n, m = map(int, input().split())
paint = [[0]*100 for x in range(100)]

cnt = 0
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            paint[i][j] += 1
            if paint[i][j] == m + 1:
                cnt += 1

print(cnt)