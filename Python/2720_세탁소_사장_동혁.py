import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    money = int(input())
    coin = [25, 10, 5, 1]
    ls = []
    for i in range(4):
        ls.append(money//coin[i])
        money = money%coin[i]
    print(*ls)