# 메모리 초과: 에라토스테네스의 체 쓰기에 숫자가 너무 큼

def collectPrime(n):
    for i in range(2, 10**n):
        if check[i]:
            primes.add(str(i))
            tmp = i
            while tmp < 10**n:
                check[tmp] = False
                tmp += i           

n = int(input())
primes = set()
check = [True]*10**n
collectPrime(n)

for i in range(10**(n-1), 10**n):
    stringNum = str(i)
    flag = True
    for j in range(n):
        if stringNum[:j+1] not in primes:
            flag = False
    if flag:
        print(stringNum)