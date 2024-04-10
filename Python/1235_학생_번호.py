import sys
ipnut = sys.stdin.readline

n = int(input())
ls = []
for _ in range(n):
    ls.append(str(input()))

for i in range(1, len(ls[0])+1):
    tmp = set()
    cnt = 0
    for j in range(n):
        if ls[j][-i:] in tmp:
            break
        else:
            tmp.add(ls[j][-i:])
            cnt += 1
    if cnt == n:
        print(i)
        break