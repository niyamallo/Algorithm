import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([False]*n)
cicle = 0
cntZero = belt.count(0)

while cntZero < k:
    cicle += 1

    belt.rotate()
    robot.rotate()
    robot[-1] = False

    for i in range(n-2, -1, -1):
        if robot[i] and not robot[i+1] and belt[i+1]:
            robot[i], robot[i+1] = False, True
            belt[i+1] -= 1
            if not belt[i+1]:
                cntZero += 1
    robot[-1] = False

    if belt[0]:
        robot[0] = True
        belt[0] -= 1
        if not belt[0]:
            cntZero += 1

print(cicle)