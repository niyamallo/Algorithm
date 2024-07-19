import sys; input = sys.stdin.readline

n = int(input())
ls = []
for i in range(n):
    ls.append(list(map(int, input().split())))
x_max = -10000
x_min = 10000
y_max = -10000
y_min = 10000

for i in range(n):
    if ls[i][0] > x_max:
        x_max = ls[i][0]
    if ls[i][0] < x_min:
        x_min = ls[i][0]
    if ls[i][1] > y_max:
        y_max = ls[i][1]
    if ls[i][1] < y_min:
        y_min = ls[i][1]
        
print((x_max-x_min)*(y_max-y_min))