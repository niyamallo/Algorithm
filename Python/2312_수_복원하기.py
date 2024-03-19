import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    num = int(input())
    dict = {}

    for i in range(2, num+1):
        cnt = 0
        while True:
            if num%i == 0:
                cnt += 1
                num = num//i
            else:
                break
        if cnt != 0:
            dict[i] = cnt

    for i in dict:
        print(i, dict[i])