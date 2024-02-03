import sys
input = sys.stdin.readline

n = int(input())
dasom = int(input())
cnt = 0

if n > 1:
    people = []
    for i in range(n-1):
        people.append(int(input()))
    people.sort()


    while dasom <= people[-1]:
        cnt += 1
        dasom += 1
        people[-1] -= 1
        people.sort()

print(cnt)
