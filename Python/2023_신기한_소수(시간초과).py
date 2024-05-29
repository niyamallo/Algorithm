def checkPrime(n):
    if n == 1:
        return False
    flag = True
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            flag = False
    return flag

n = int(input())
for i in range(10**(n-1), 10**n):
    stringNum = str(i)
    flag = True
    for j in range(n):
        if not checkPrime(int(stringNum[:j+1])):
            flag = False
            break
    if flag:
        print(i)