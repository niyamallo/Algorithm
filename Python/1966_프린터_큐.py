import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    ls = list(map(int, input().split()))
    dq = deque(ls)
    ls.sort()
    cnt = 0
    idx = -1
    while True:
        big = ls[idx]
        if dq[0] == big:
            dq.popleft()
            idx -= 1
            cnt += 1
            if m == 0:
                print(cnt)
                break
            m -= 1
        else:
            dq.append(dq.popleft())
            m -= 1
            if m < 0:
                m = len(dq) - 1