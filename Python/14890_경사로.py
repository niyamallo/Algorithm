import sys
input = sys.stdin.readline

N, L = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
count = 0

for i in range(N):
    stair = Map[i]
    now = 0
    high = stair[0]
    can_up = 0
    flag = True
    while now < N:
        if stair[now] == high:
            can_up += 1
        elif stair[now] == high + 1:
            if can_up >= L:
                high += 1
                can_up = 1
            else:
                flag = False
                break
        elif stair[now] == high - 1:
            if now + L < N + 1:
                for next in stair[now+1:now+L]:
                    if next != stair[now]:
                        flag = False
                        break
                now += L - 1
                high -= 1
                can_up = 0
            else:
                flag = False
                break
        else:
            flag = False
        now += 1
    if flag:
        count += 1

for i in range(N):
    stair = []
    for j in range(N):
        stair.append(Map[j][i])
    now = 0
    high = stair[0]
    can_up = 0
    flag = True
    while now < N:
        if stair[now] == high:
            can_up += 1
        elif stair[now] == high + 1:
            if can_up >= L:
                high += 1
                can_up = 1
            else:
                flag = False
                break
        elif stair[now] == high - 1:
            if now + L < N + 1:
                for next in stair[now+1:now+L]:
                    if next != stair[now]:
                        flag = False
                        break
                now += L - 1
                high -= 1
                can_up = 0
            else:
                flag = False
                break
        else:
            flag = False
        now += 1
    if flag:
        count += 1

print(count)