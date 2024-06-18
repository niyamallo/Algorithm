n, l = map(int, input().split())

for i in range(l, 101):
    xi = n - (i * (i + 1) // 2)
    if xi % i == 0:
        x = xi // i
        if x + 1 >= 0:
            print(*[x for x in range(x+1, x+i+1)])
            break
else:
    print(-1)