import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
check = True

if n == 1:
    print("A")
elif n == 2:
    if ls[0] == ls[1]:
        print(ls[0])
    else:
        print("A")
else:
    if ls[1]-ls[0] == 0:
        a = 1
    else:
        a = (ls[2]-ls[1])//(ls[1]-ls[0])
    b = (ls[1]-a*ls[0])

    for i in range(1, n):
        if ls[i] != a*ls[i-1] + b:
            check = False
            break
    if check:
        print(a*ls[-1] + b)
    else:
        print("B")