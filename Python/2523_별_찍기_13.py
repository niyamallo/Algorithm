n = int(input())

for i in range(2*n-1):
    print("*"*(n-abs(n-1-i)))