from collections import deque
change = [1, 4, 6, 3]
switch = deque()
switch.append(5)
total = 0

n, m = map(int, input().split())
for i in range(n):
    total += sum(change)*(m//4) + sum(change[0:m%4])
    switch.append(7-change[m%4-1])
    next = switch.popleft()
    change = [next, change[-2+m%4], 7-next, 7-change[-2+m%4]]
print(total)