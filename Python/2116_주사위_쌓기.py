import sys; input = sys.stdin.readline

def check_biggest_num(a, b):
    for i in range(6, 0, -1):
        if i != a and i != b:
            return i
        
n = int(input())
dice = [list(map(int, input().split())) for _ in range(n)]
opposite = [5, 3, 4, 1, 2, 0]
answer = 0
for i in range(6):
    down = dice[0][i]
    up = dice[0][opposite[i]]
    total = check_biggest_num(down, up)
    for j in range(1, n):
        down = up
        up = dice[j][opposite[dice[j].index(down)]]
        total += check_biggest_num(down, up)
    if total > answer:
        answer = total

print(answer)
