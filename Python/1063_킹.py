import sys
input = sys.stdin.readline

king, stone, n = input().split()
rows = "0ABCDEFGH"

king = [rows.index(king[0]), int(king[1])]
stone = [rows.index(stone[0]), int(stone[1])]
n = int(n)

def moving(piece, x):
    row = piece[0]
    column = piece[1]
    if x == "R":
        row += 1
    elif x == "L":
        row -= 1
    elif x == "B":
        column -= 1
    elif x == "T":
        column += 1
    elif x == "RT":
        row += 1
        column += 1
    elif x == "LT":
        row -= 1
        column += 1
    elif x == "RB":
        row += 1
        column -= 1
    elif x == "LB":
        row -= 1
        column -= 1
    return [row, column]
        

for _ in range(n):
    tmp_king = king
    tmp_stone = stone
    move = input().rstrip()
    new_king = moving(king, move)
    if 0 < new_king[0] < 9 and 0 < new_king[1] < 9:
        king = new_king
    if king == stone:
        new_stone = moving(stone, move)
        if 0 < new_stone[0] < 9 and 0 < new_stone[1] < 9:
            stone = new_stone
    if tmp_stone == stone and king == stone:
        king = tmp_king

king = rows[king[0]] + str(king[1])
stone = rows[stone[0]] + str(stone[1])

print(king)
print(stone)