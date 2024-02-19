import sys
input = sys.stdin.readline

n = int(input())
fac = 1
for i in range(1, n+1):
    fac *= i
str_fac = str(fac)

cnt = 0
for i in range(len(str_fac), 0, -1):
    if str_fac[i-1] == "0":
        cnt += 1
    else:
        break

print(cnt)