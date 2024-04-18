a, b = map(int, input().split())

cnt = 1
num = 1
ans = 0
checked = False

while cnt <= b:
    for _ in range(num):
        if cnt >= a:
            ans += num
        if cnt >= b:
            checked = True
            break
        cnt += 1
    if checked:
        break
    num += 1

print(ans)