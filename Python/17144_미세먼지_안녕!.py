import sys
from collections import deque
input = sys.stdin.readline

def check_dust():
    for i, line in enumerate(room):
        for j, value in enumerate(line):
            if value > 0:
                dust.append((i, j, value))

def spread():
    while dust:
        x, y, value = dust.popleft()
        cnt = 0
        tmp_value = value//5
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or R<=nx or ny<0 or C<=ny:
                continue
            if room[nx][ny] == -1:
                continue
            cnt += 1
            room[nx][ny] += tmp_value
        room[x][y] -= cnt*tmp_value

def clean():
    x, y = cleaner[0], 1
    index = 1
    tmp = 0
    while True:
        nx = x + dx[index]
        ny = y + dy[index]
        if nx == R or ny == C or nx == -1 or ny == -1:
            index = (index-1)%4
            continue
        if x == cleaner[0] and y == 0:
            break
        room[x][y], tmp = tmp, room[x][y]
        x, y = nx, ny
    
    x, y = cleaner[1], 1
    index = 1
    tmp = 0
    while True:
        nx = x + dx[index]
        ny = y + dy[index]
        if nx == R or ny == C or nx == -1 or ny == -1:
            index = (index+1)%4
            continue
        if x == cleaner[1] and y == 0:
            break
        room[x][y], tmp = tmp, room[x][y]
        x, y = nx, ny

def total():
    total = 2
    for i in range(R):
        for j in range(C):
            total += room[i][j]

    return total

R, C, T = map(int, input().split())
room =  []
cleaner = []
cleaner_checker = False
for i in range(R):
    room_line = list(map(int, input().split()))
    if not cleaner_checker and -1 in room_line:
        cleaner.append(i)
        cleaner.append(i+1)
        cleaner_checker = True
    room.append(room_line)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dust = deque()

for _ in range(T):
    check_dust()
    spread()
    clean()

print(total())