n = int(input())
cnt = 0
num = 0

while num <= n:
    cnt += 1
    num += cnt

print(cnt-1)