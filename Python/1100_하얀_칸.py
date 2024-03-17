import sys
input = sys.stdin.readline

board = []
for _ in range(8):
    line = list(input().rstrip())
    board.append(line)

cnt = 0
for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0 and board[i][j] == "F":
            cnt += 1

print(cnt)