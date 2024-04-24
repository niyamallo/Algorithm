import sys
input = sys.stdin.readline

n, m = map(int, input().split())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().rstrip())))

total = 0
for i in range(1<<n*m):
    tmp_total = 0
    
    for row in range(n):
        row_total = 0
        for col in range(m):
            idx = row*m + col
            if i&(1<<idx) != 0:
                row_total = 10*row_total + paper[row][col]
            else:
                tmp_total += row_total
                row_total = 0
        tmp_total += row_total
    
    for col in range(m):
        col_total = 0
        for row in range(n):
            idx = row*m + col
            if i&(1<<idx) == 0:
                col_total = 10*col_total + paper[row][col]
            else:
                tmp_total += col_total
                col_total = 0
        tmp_total += col_total
    if total < tmp_total:
        total = tmp_total

print(total)