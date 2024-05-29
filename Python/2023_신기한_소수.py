from collections import deque

def checkPrime(n):
    if n == 1:
        return False
    flag = True
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            flag = False
            break
    return flag

def bfs(n):
    dq = deque()
    for i in range(2, 10):
        if checkPrime(i):
            dq.append(str(i))
    while dq:
        now = dq.popleft()
        if len(now) == n:
            print(now)
        else:
            for j in range(0,10):
                new = now + str(j)
                if checkPrime(int(new)):
                    dq.append(new)
                    
n = int(input())
bfs(n)