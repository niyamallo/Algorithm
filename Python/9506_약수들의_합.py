import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1:
        break
    else:
        ls = []
        for i in range(1, n//2+1):
            if n%i == 0:
                ls.append(i)
        if sum(ls) == n:
            print(f'{n} = {" + ".join(str(x) for x in ls)}')
        else:
            print(f'{n} is NOT perfect.')