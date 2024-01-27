import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(input().rstrip()))

ans = []
for i in range(N-7):
    for j in range(M-7):
        paint_1 = 0
        paint_2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b)%2 == 0:
                    if board[a][b] == "B":
                        paint_1 += 1
                    else:
                        paint_2 += 1
                else:
                    if board[a][b] == "W":
                        paint_1 += 1
                    else:
                        paint_2 += 1
        ans.append(paint_1)
        ans.append(paint_2)

print(min(ans))