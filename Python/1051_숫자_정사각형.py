import sys
input = sys.stdin.readline

def check(s):
    for i in range(n-s+1):
        for j in range(m-s+1):
            if board[i][j] == board[i+s-1][j+s-1] == board[i][j+s-1] == board[i+s-1][j]:
                return True
            
n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().rstrip())))

size = min(n, m)
for s in range(size, 0, -1):
    if check(s):
        print(s**2)
        break