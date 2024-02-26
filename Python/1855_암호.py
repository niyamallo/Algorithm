import sys
input = sys.stdin.readline

n = int(input())
string = input().rstrip()
loop = len(string) // n
ans1 = ""

for i in range(loop):
    cnt = i*n
    if i % 2 == 0:
        for j in range(n):
            ans1 += string[cnt + j]
    else:
        for j in range(n):
            ans1 += string[cnt + n - 1 - j]

ans2 = ""

for i in range(n):
    for j in range(loop):
        ans2 += ans1[j * n + i]

print(ans2)