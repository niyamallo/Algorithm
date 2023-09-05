from collections import deque
import sys

n = int(input())
dq = deque()
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        dq.appendleft(command[1])
    elif command[0] == 'push_back':
        dq.append(command[1])
    elif command[0] == 'pop_front':
        if len(dq):
            print(dq.popleft())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if len(dq):
            print(dq.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        if len(dq):
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if len(dq):
            print(dq[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(dq):
            print(dq[-1])
        else:
            print(-1)



