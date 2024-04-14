from collections import deque

a, b = map(int, input().split())
dq = deque()
dq.append((a, 1))
checked = False

while dq:
    now, cnt = dq.popleft()
    if now == b:
        checked = True
        print(cnt)
        break
    if now > b:
        continue
    dq.append((now*2, cnt+1))
    dq.append((int(str(now)+"1"), cnt+1))

if not checked:
    print(-1)