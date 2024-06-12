import sys
input = sys.stdin.readline

def tornado_90(tornado):
    return list(reversed(list(zip(*tornado))))

def spread(x, y, direction):
    global outer_sand
    sand = sand_map[x][y]
    left_sand = sand
    sand_map[x][y] = 0
    for i in range(5):
        for j in range(5):
            now_sand = int(sand * tornado[direction][i][j])
            left_sand -= now_sand
            if 0 <= x + i - 2 < n and 0 <= y + j - 2 < n:
                sand_map[x + i - 2][y + j - 2] += now_sand
            else:
                outer_sand += now_sand
    if 0 <= x + dx[direction] < n and 0 <= y + dy[direction] < n:
        sand_map[x + dx[direction]][y + dy[direction]] += left_sand
    else:
        outer_sand += left_sand

t1 = [[0, 0, 0.02, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0.05, 0, 0, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0, 0, 0.02, 0, 0]]
t2 = tornado_90(t1)
t3 = tornado_90(t2)
t4 = tornado_90(t3)
tornado = [t1, t2, t3, t4]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

n = int(input())
sand_map = []
for _ in range(n):
    sand_map.append(list(map(int, input().split())))

outer_sand = 0
direction = 0
x = n // 2
y = n // 2
distance = 1
flag = True

while not (x == 0 and y == -1):

    for i in range(distance):
        x += dx[direction]
        y += dy[direction]
        spread(x, y, direction)
    direction = (direction + 1) % 4
    if flag:
        flag = False
    else:
        flag = True
        distance += 1

print(outer_sand)