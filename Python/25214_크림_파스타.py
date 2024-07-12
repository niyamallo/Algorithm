import sys; input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
answer = [0]*n
min_num = ls[0]

for i in range(1, n):
    if ls[i-1] >= ls[i]:
        answer[i] = answer[i-1]
        if min_num > ls[i]:
            min_num = ls[i]
    else:
        answer[i] = max(ls[i] - min_num, answer[i-1])

print(*answer)