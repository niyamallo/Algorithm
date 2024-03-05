import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nx, ny = n//4, n%4
if ny == 0:
    nx -= 1
    ny = 4
mx, my = m//4, m%4
if my == 0:
    mx -= 1
    my = 4

print(abs(nx-mx) + abs(ny-my))