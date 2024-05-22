import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
answer = [0]*n

for i in range(n):
    cnt = 0
    for j in range(n):
        if answer[j] == 0:
            if cnt == ls[i]:
                answer[j] = i+1
                break
            else:
                cnt += 1
print(*answer)
