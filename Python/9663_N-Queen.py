def isPossible(x, depth):
    for i in range(1,depth+1):
        if board[depth-i] == x:
            return False
        if board[depth-i] == x - i:
            return False
        if board[depth-i] == x + i:
            return False
    return True

def nQueen(depth):
    global answer
    if len(board) == n:
        answer += 1
        return
    else:
        for i in range(n):
            if isPossible(i, depth+1):
                board.append(i)
                nQueen(depth+1)
                board.pop()
                
n = int(input())
answer = 0
for i in range(n):
    board = [i]
    nQueen(0)

print(answer)
